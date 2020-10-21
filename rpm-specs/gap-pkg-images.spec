%global pkgname images

Name:           gap-pkg-%{pkgname}
Version:        1.3.0
Release:        2%{?dist}
Summary:        Minimal and canonical images in permutation groups

License:        MPLv2.0
URL:            https://gap-packages.github.io/images/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-ferret
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-tomlib

Requires:       gap-core

Recommends:     gap-pkg-ferret

%description
This package provides functionality to compute canonical representatives
under group actions in GAP.

%package doc
Summary:        Images documentation
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Update the atlas package name
sed -i 's/atlas/atlasrep/' tst/test_functions.g

%build
export LC_ALL=C.UTF-8
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version}
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{LICENSE,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 30 2020 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- Initial RPM
