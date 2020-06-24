%global pkgname  zeromqinterface
%global upname   ZeroMQInterface

Name:           gap-pkg-%{pkgname}
Version:        0.12
Release:        3%{?dist}
Summary:        ZeroMQ bindings for GAP

License:        GPLv2+
URL:            https://gap-packages.github.io/%{upname}/
Source0:        https://github.com/gap-packages/%{upname}/releases/download/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  python3-devel

Requires:       gap-core%{?_isa}

%description
This package provides both low-level bindings as well as some higher
level interfaces for the ZeroMQ message passing library for GAP and
HPC-GAP, enabling lightweight distributed computation.

%package doc
Summary:        Documentation for ZeroMQ bindings for GAP
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

# Fix python shebang
sed -i.orig 's,%{_bindir}/env python,%{__python3},' zgap
touch -r zgap.orig zgap
rm zgap.orig

%build
export LC_ALL=C.UTF-8
%configure --with-gaproot=%{_gap_dir} --disable-silent-rules

# Get rid of undesirable hardcoded rpaths
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

%make_build

# Build the documentation
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}
cp -a bin doc gap tst *.g %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

mkdir -p %{buildroot}%{_gap_dir}/bin
cp -p zgap %{buildroot}%{_gap_dir}/bin

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%license COPYRIGHT.md LICENSE
%{_gap_dir}/bin/zgap
%{_gap_dir}/pkg/%{upname}-%{version}/
%exclude %{_gap_dir}/pkg/%{upname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{upname}-%{version}/doc/
%{_gap_dir}/pkg/%{upname}-%{version}/doc/

%changelog
* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 0.12-3
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov  2 2019 Jerry James <loganjerry@gmail.com> - 0.12-1
- Version 0.12

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 0.11-2
- Rebuild for changed bin dir name in gap 4.10.1

* Wed Feb 27 2019 Jerry James <loganjerry@gmail.com> - 0.11-1
- Initial RPM
