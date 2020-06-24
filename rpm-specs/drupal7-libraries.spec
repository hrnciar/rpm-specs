%{?drupal7_find_provides_and_requires}

%global module libraries

Name:          drupal7-%{module}
Version:       2.3
Release:       9%{?dist}
Summary:       Allows version-dependent and shared usage of external libraries

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# libraries.info
Requires:      drupal7(system) >= 7.11
# phpcompatinfo (computed from version 2.3)
# <none>


%description
Drupal 7 only has built-in support for non-external libraries via
hook_library(). But it is only suitable for drupal.org projects that bundle
their own library; i.e., the module author is the creator and vendor of the
library. Libraries API should be used for externally developed and
distributed libraries. A simple example would be a third-party jQuery
plugin.

This package provides the following Drupal module:
* %{module}


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
# Docs used at runtime
#mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
# Docs used at runtime
#%%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3-9
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 04 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.3-1
- Updated to 2.3 (RHBZ #1327693)
- Minor spec cleanups

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 15 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.2-1
- Updated to 2.2 (BZ #1063727; release notes https://drupal.org/node/2192173)
- Spec cleanup

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Peter Borsa <peter.borsa@gmail.com> - 2.1-1
- Update to 2.1

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 11 2012 Scott Dodson <sdodson@redhat.com> - 2.0-0
- Update to 2.0
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 7 2011 Scott Dodson <sdodson@redhat.com> - 1.0-1
- Initial Drupal 7 package
