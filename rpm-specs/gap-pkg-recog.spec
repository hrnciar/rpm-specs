# The 1.3.2 release fails multiple tests with GAP 4.11.  Until a new version is
# released, we build from git.
%global commit      168ed6258502ed24a14e284d275b3f50b9f07de3
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20200127

%global pkgname recog

Name:           gap-pkg-%{pkgname}
Version:        1.3.2
Release:        4.%{gitdate}.%{shortcommit}%{?dist}
Summary:        Group recognition methods

License:        GPLv3+
URL:            https://gap-packages.github.io/%{pkgname}/
#Source0:        https://github.com/gap-packages/%%{pkgname}/releases/download/v%%{version}/%%{pkgname}-%%{version}.tar.bz2
Source0:        https://github.com/gap-packages/%{pkgname}/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
# Predownloaded data from ATLAS needed for the tests
Source1:        %{name}-testdata.tar.xz

BuildArch:      noarch
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-factint
BuildRequires:  gap-pkg-forms
BuildRequires:  gap-pkg-genss
BuildRequires:  gap-pkg-orb
BuildRequires:  gap-pkg-tomlib

Requires:       gap-pkg-atlasrep
Requires:       gap-pkg-factint
Requires:       gap-pkg-forms
Requires:       gap-pkg-genss
Requires:       gap-pkg-orb

%description
This is a GAP package for group recognition.

%package doc
Summary:        Recog documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{commit}
%setup -q -n %{pkgname}-%{commit} -T -D -b 1

%build
export LC_ALL=C.UTF-8
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{commit} %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/misc
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{.mailmap,CHANGES,LICENSE,Makefile,NOTES,README.md,TODO,WISHLIST}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8

# Tell ATLAS where to find downloaded files
mkdir ~/.gap
cat > ~/.gap/gap.ini << EOF
SetUserPreference( "atlasrep", "AtlasRepDataDirectory", "%{_builddir}/atlasrep/" );
EOF

gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES NOTES README.md TODO WISHLIST
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%changelog
* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 1.3.2-4.20200127.168ed62
- Rebuild for gap 4.11.0
- Add missing gap-pkg-orb dependency

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Jerry James <loganjerry@gmail.com> - 1.3.2-2
- Drop the ctbllib and tomlib dependencies

* Thu Oct 24 2019 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- Initial RPM
