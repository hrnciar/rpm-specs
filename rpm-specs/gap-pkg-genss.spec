%global pkgname genss

Name:           gap-pkg-%{pkgname}
Version:        1.6.6
Release:        4%{?dist}
Summary:        Randomized Schreier-Sims algorithm

License:        GPLv3+
URL:            https://gap-packages.github.io/genss/
Source0:        https://github.com/gap-packages/genss/releases/download/v%{version}/%{pkgname}-%{version}.tar.bz2
BuildArch:      noarch

# The AtlasRep, TomLib, and CtblLib dependencies are needed for the tests only
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-orb-doc
BuildRequires:  gap-pkg-tomlib

Requires:       gap-pkg-io
Requires:       gap-pkg-orb

%description
The genss package implements the randomized Schreier-Sims algorithm to
compute a stabilizer chain and a base and strong generating set for
arbitrary finite groups.

%package doc
Summary:        Genss documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-orb-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Fix encodings
for fil in init.g read.g doc/examples.xml doc/intro.xml; do
  iconv -f iso8859-1 -t utf-8 $fil > $fil.utf8
  touch -r $fil $fil.utf8
  mv -f $fil.utf8 $fil
done

%build
export LC_ALL=C.UTF-8
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
ln -s %{_gap_dir}/pkg/orb* ../pkg
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg

# Fix references to the build directory
sed -i "s,$PWD/\.\./pkg,../..,g" doc/*.html

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
cp -a doc examples gap test tst *.g %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES README
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
* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 1.6.6-4
- Add tomlib BR to eliminate build warnings

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov  5 2019 Jerry James <loganjerry@gmail.com> - 1.6.6-2
- Bump and rebuild due to update snafu

* Mon Aug 12 2019 Jerry James <loganjerry@gmail.com> - 1.6.6-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb  2 2019 Jerry James <loganjerry@gmail.com> - 1.6.5-5
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan  8 2018 Jerry James <loganjerry@gmail.com> - 1.6.5-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.6.4-1
- New upstream version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  8 2016 Jerry James <loganjerry@gmail.com> - 1.6.3-1
- New upstream version
- Update URLs

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.6.2-2
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Turn test failures into build failures

* Tue Jul 28 2015 Jerry James <loganjerry@gmail.com> - 1.6.2-1
- Initial RPM
