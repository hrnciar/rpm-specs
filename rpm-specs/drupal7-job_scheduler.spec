%{?drupal7_find_provides_and_requires}

%global module job_scheduler

Name:          drupal7-%{module}
Version:       2.0
Release:       6%{?pre_release:.%{pre_release}}%{?dist}
Summary:       Simple API for scheduling tasks

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}%{?pre_release:-%{pre_release}}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 2.0)
Requires:      php-date
Requires:      php-pcre

%description
Simple API for scheduling tasks once at a predetermined time or periodically at
a fixed interval.

This package provides the following Drupal modules:
* %{module}
* %{module}_trigger


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-6
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 24 2018 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-1
- Update to 2.0 (RHBZ #1544736)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.13.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.12.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.11.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 01 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.10.alpha3
- Minor cleanups
- Removed %%defattr

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-0.9.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.8.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 18 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.0-0.7.alpha3
- Spec cleanup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.6.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.5.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.4.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.3.alpha3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Jared Smith <jsmith@fedoraproject.org> - 2.0-0.1.alpha3
- Initial packaging

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-0.2.alpha2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 23 2011 Peter Borsa <peter.borsa@gmail.com> - 2.0-0.1.alpha2
- Initial packaging
