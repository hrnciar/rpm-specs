%global pkgname ferret

Name:           gap-pkg-%{pkgname}
Version:        1.0.3
Release:        2%{?dist}
Summary:        Backtracking search in permutation groups

# The project as a whole is MPLv2.0.
# YAPB++/source/library/fnv_hash.hpp is Public Domain.
License:        MPLv2.0 and Public Domain
URL:            https://gap-packages.github.io/ferret/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc-c++
BuildRequires:  libtool

Requires:       gap-core%{?_isa}

%description
Ferret is a reimplementation of parts of Jeffery Leon's Partition
Backtrack framework in C++, with extensions including:

- Ability to intersect many group simultaneously.
- Improved refiners based on orbital graphs.

This package currently supports:

- Group intersection.
- Stabilizing many structures including sets, sets of sets, graphs,
  sets of tuples and tuples of sets.

This package can be used by users in two ways:

- When the package is loaded many built-in GAP functions such as
  'Intersection' and 'Stabilizer' are replaced with more optimized
  implementations.  This requires no changes to existing code.

- The function 'Solve' provides a unified interface to accessing
  all the functionality of the package directly.

%package doc
Summary:        Ferret documentation
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Update the atlas package name
sed -i 's/atlas/atlasrep/' tst/test_functions.g

# Ensure that the bundled gason is not used
rm -fr YAPB++/simple_graph/gason

%build
export LC_ALL=C.UTF-8
%configure --with-gaproot=%{_gap_dir}
%make_build

# Build the documentation
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version}
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -p bin/%{_gap_arch}/.libs/ferret.so \
   %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -a doc lib tst *.g %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3
- Replace GPLv2+ with MPLv2.0 in the License field

* Thu Apr 30 2020 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- Initial RPM
