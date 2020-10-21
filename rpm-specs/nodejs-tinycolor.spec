%global npm_name tinycolor

Summary:       A to-the-point color module for node
Name:          nodejs-%{npm_name}
Version:       0.0.1
Release:       15%{?dist}
License:       MIT
URL:           http://github.com/einaros/tinycolor
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
# The readme file has been updated to include the license.
# We are including it here until the next release when it should be
#   part of the release.
# https://raw.github.com/einaros/tinycolor/master/README.md
Source1:       nodejs-tinycolor-README.md
BuildRequires: nodejs-devel
BuildArch:     noarch

%description
This is a no-fuzz, bare bones color module for nodejs.

%prep
%setup -q -n package

rm -f README.md
cp -pr %{SOURCE1} README.md

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr tinycolor.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%doc README.md example.js
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 28 2013 Troy Dawson <tdawson@redhat.com> - 0.0.1-3
- Fixed description so words are spelled correctly
- Updated README.md with the latest one that has a license

* Fri Mar 01 2013 Troy Dawson <tdawson@redhat.com> - 0.0.1-2
- Update spec to Fedora nodejs standards

* Wed Nov 14 2012 Troy Dawson <tdawson@redhat.com> - 0.0.1-1
- Initial build using tchor spec template
