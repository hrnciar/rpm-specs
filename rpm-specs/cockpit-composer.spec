# This spec file has been automatically updated
Version:        21
Release: 1%{?dist}
Name:           cockpit-composer
Summary:        Composer GUI for use with Cockpit

License:        MIT
URL:            http://weldr.io/
Source0:        https://github.com/osbuild/cockpit-composer/releases/download/%{version}/cockpit-composer-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  libappstream-glib

Requires:       cockpit
Requires:       weldr
Suggests:       osbuild-composer >= 14

%description
Composer generates custom images suitable for deploying systems or uploading to
the cloud. It integrates into Cockpit as a frontend for osbuild.

%prep
%setup -q -n cockpit-composer

%build
# Nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/cockpit/composer
cp -a public/dist/* %{buildroot}/%{_datadir}/cockpit/composer
mkdir -p %{buildroot}/%{_datadir}/metainfo/
appstream-util validate-relax --nonet io.weldr.cockpit-composer.metainfo.xml
cp -a io.weldr.cockpit-composer.metainfo.xml %{buildroot}/%{_datadir}/metainfo/

%files
%doc README.md
%license LICENSE.txt
%{_datadir}/cockpit/composer
%{_datadir}/metainfo/*

%changelog
* Sun Jun 14 2020 Lars Karlitski <lars@karlitski.net> - 21-1

- Support setting parameters (ref and parent) for ostree images
- Loosen restrictions on password strength
- Various UI refinements

* Mon Jun 08 2020 Lars Karlitski <lars@karlitski.net> - 20-1

- Fix various missing translations
- Improve message when a blueprint is empty
- Hide logs button until logs are available
- Update test framework to be closer to that of other cockpit projects

* Wed Jun 03 2020 Jacob Kozol <jacobdkozol@gmail.com> - 19-1

- Minor UI improvements for the images list view and the images dropdown

- Fixes to the password tests

- Prepartion for future osbuild support

- Minor NPM updates for react

- Minor translation updates

* Wed May 20 2020 Jacob Kozol <jacobdkozol@gmail.com> - 18-1

- Fix flake8 E302 error in tests

- Minor NPM updates for patternfly and jquery

- Translations updates

* Wed May 06 2020 Jacob Kozol <jacobdkozol@gmail.com> - 17-1

- The support for uploading VHD images to Azure is now available.

- Help text is now provided for all AWS fields. This texts explains what
  each field represents and where to find their values in the AWS
  web console.

- The image size can now be specified when creating an image.

- Tests are refactored to run on Cockpit's testing framework. All tests
  have been moved away from selenium.

- Minor NPM updates

* Wed Apr 15 2020 Jacob Kozol <jacobdkozol@gmail.com> - 16-1

- The ability to upload to AWS has been added. The create image modal is
  replaced with a wizard enabling additional customizations and
  functionality. If the user creates an AMI the user can also enter the
  credentials and parameters needed to upload this image to EC2 in AWS.

- Cockpit-composer has migrated from Weldr to the OSBuild github
  organization. It can now be found at osbuild/cockpit-composer instead
  of weldr/cockpit-composer.

- Minor NPM updates have been made for React and Patternfly

* Wed Apr 01 2020 Jacob Kozol <jacobdkozol@gmail.com> - 15-1

- Migrate from lorax-composer to osbuild-composer backend
- Update tests for new backend
- Improve stability of tests
- Remove Zanata from Travis configuration
- Update NPM dependencies

* Wed Mar 18 2020 Jacob Kozol <jacobdkozol@gmail.com> - 14-1

- Test against lorax-composer explicitly
- Update NPM dependencies

* Wed Mar 04 2020 Jacob Kozol <jacobdkozol@gmail.com> - 13-1

- Update translations
- Update NPM dependencies

* Wed Feb 19 2020 Martin Pitt <martin@piware.de> - 12.1-1

- Fix integration tests, external test repository URL ceased to exist

* Wed Feb 19 2020 Martin Pitt <martin@piware.de> - 12-1

- Translation updates
- Add documentation URL page help menu

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Martin Pitt <martin@piware.de> - 11-1

- Update translations
- Fix tests to work against current Cockpit as non-root

* Tue Dec 17 2019 Lars Karlitski <lars@karlitski.net> - 10-1

- Show depsolve errors on the blueprints page
- Add labels for additional output types
- Convert more components to PF4

* Fri Oct 25 2019 Martin Pitt <martin@piware.de> - 9-1

- Translation updates
- Expose Image Builder on /composer, not /welder
- NPM dependency updates

* Wed Oct 02 2019 Martin Pitt <martin@piware.de> - 8-1

- NPM dependency updates

* Fri Sep 06 2019 Jacob Kozol <jacobdkozol@gmail.com> - 7-1
- Define a URL for each tab on a blueprint page
- Provide a link in the image creation notification to the Images tab on the blueprint page

* Wed Aug 21 2019 Jacob Kozol <jacobdkozol@gmail.com> - 6-1
- Text string updates

* Wed Aug 07 2019 Jacob Kozol <jacobdkozol@gmail.com> - 5-1

- Fix PropTypes for the homepage
- Code clean up for the list of components

* Wed Jul 31 2019 Martin Pitt <martin@piware.de> - 4-1

- Fix AppStream ID
- Translation updates

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Martin Pitt <martin@piware.de> - 3-1

- Use cockpit's PatternFly CSS, to pick up the new PatternFly 4 styling
- Add additional blueprint name validation
- Fix images not loading on refresh
- Add notification for source repo deletion

* Wed Jun 26 2019 Martin Pitt <martin@piware.de> - 2-1

- Strip newlines from SSH keys before saving
- Translation updates

* Wed Jun 05 2019 Cockpit Project <cockpituous@gmail.com> - 1-1
- Update to upstream 1 release

* Fri May 24 2019 Cockpit Project <cockpituous@gmail.com> - 0.4-1
- Update to upstream 0.4 release

* Mon May 06 2019 Cockpit Project <cockpituous@gmail.com> - 0.3-1
- Update to upstream 0.3 release

* Mon Apr 15 2019 Cockpit Project <cockpituous@gmail.com> - 0.2.1-1
- Update to upstream 0.2.1 release

* Mon Mar 25 2019 Cockpit Project <cockpituous@gmail.com> - 0.2.0-1
- Update to upstream 0.2.0 release

* Thu Mar 07 2019 Cockpit Project <cockpituous@gmail.com> - 0.1.9-2
- Update to upstream 0.1.9 release

