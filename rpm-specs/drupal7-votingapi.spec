%{?drupal7_find_provides_and_requires}

%global module votingapi

Name:          drupal7-%{module}
Version:       2.12
Release:       14%{?dist}
Summary:       Provides a shared voting API for other modules

License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.70-2

# phpcompatinfo (computed from version 2.12)
# <none>

%description
VotingAPI helps developers who want to use a standardized API and schema for
storing, retrieving, and tabulating votes for Drupal content.

Among other things, it supports:
* Rating of any content (comments, nodes, users, fish, whatever)
* Multi-criteria voting (rate a game based on video, audio, and replayability)
* Automatic tabulation of results (with support for different voting styles,
  like 'percentage' and '+1/-1')
* Efficient caching of results (sorting and filtering doesn't require any
  recalculation)
* Hooks for additional vote calculations

Note that this module does NOT directly expose any voting mechanisms to end
users. It's a framework designed to make life easier for other developers,
and to standardize voting data for consumption by other modules (like Views).

For some examples of simple voting systems based on VotingAPI, check
Is Useful [1], Fivestar [2], and Plus1 [3].

This package provides the following Drupal module:
* %{module}

[1] http://drupal.org/project/is_useful
[2] http://drupal.org/project/fivestar
[3] http://drupal.org/project/plus1


%prep
%setup -qn %{module}

: Licenses and docs
mkdir -p .rpm/{licenses,docs}
mv LICENSE.txt .rpm/licenses/
mv *.txt .rpm/docs/


%build
# Empty build section, nothing to build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/



%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{drupal7_modules}/%{module}


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.12-13
- Bump build requires drupal7-rpmbuild to ">= 7.70-2" to fix F32+ auto provides

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 02 2016 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.12-5
- Minor spec cleanups

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 31 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.12-2
- Added phpcompatinfo requires
- Updated description
- %%license usage

* Sun Aug 31 2014 Shawn Iwinski <shawn.iwinski@gmail.com> - 2.12-1
- Updated to 2.12 (BZ #1130011; release notes https://www.drupal.org/node/2321111)
- Spec cleannup

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Scott Dodson <sdodson@redhat.com> - 2.11-0
- Update to 2.11

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Peter Borsa <peter.borsa@gmail.com> - 2.10-1
- Update to 2.10

* Fri Nov 2 2012 Peter Borsa <peter.borsa@gmail.com> - 2.9-1
- Update to 2.9

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 2 2012 Scott Dodson <sdodson@redhat.com> - 2.6-1
- Update to 2.6

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 7 2011 Scott Dodson <sdodson@redhat.com> - 2.4-1
- Initial Drupal 7 package
