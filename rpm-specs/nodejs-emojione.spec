# tests are disabled due to missing packages in Fedora
%global enable_tests 0
%global module_name emojione

Name:           nodejs-%{module_name}
Version:        2.2.7
Release:        9%{?dist}
Summary:        EmojiOne is a complete set of emojis designed for the web
# Artwork included is in CC-BY-SA license
# Non-Artwork files are under MIT license
License:        MIT and CC-BY-SA
URL:            http://www.emojione.com
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
Patch1:         %name-xx-build.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  nodejs-grunt-cli
BuildRequires:  nodejs-grunt-contrib-cssmin
BuildRequires:  nodejs-grunt-contrib-jshint
BuildRequires:  nodejs-grunt-contrib-qunit
BuildRequires:  nodejs-grunt-contrib-sass
BuildRequires:  nodejs-grunt-contrib-uglify
BuildRequires:  nodejs-grunt-contrib-watch
BuildRequires:  nodejs-grunt-imageoptim
BuildRequires:  nodejs-grunt-jsonlint
BuildRequires:  nodejs-grunt-spritesmith
BuildRequires:  nodejs-grunt-svgstore
%endif

Requires:       %{name}-json = %{version}-%{release}

%description
EmojiOne is a complete set of emojis designed for the web. It includes
libraries to easily convert unicode characters to shortnames (:smile:)
and shortnames to our custom emoji images. PNG and SVG formats provided
for the emoji images.


%package json
Summary:        EmojiOne utility for Json files

%description json
This utility provides Json files which can be utilized by other packages.


%package android
Summary:        EmojiOne utility for Android
Requires:       %{name} = %{version}-%{release}

%description android
This utility provides a method to convert from shortname to unicode characters.


%package awesome
Summary:        Emojione awesome
Requires:       %{name} = %{version}-%{release}

%description awesome
EmojiOne Awesome is for front end developers who just wanna drop an emoji on a
page without using any sorts of scripts. 


%package meteor
Summary:        EmojiOne utility for Meteor
Requires:       %{name} = %{version}-%{release}

%description meteor
This utility provides a method to convert from shortname to unicode characters.


%package ios
Summary:        EmojiOne utility for iOS
Requires:       %{name} = %{version}-%{release}

%description ios
EmojiOne utility is for iOS.

%package python
Summary:        EmojiOne utility for Python
Requires:       %{name} = %{version}-%{release}

%description python
EmojiOne utility is for Python.

%package swift
Summary:        EmojiOne utility for Swift
Requires:       %{name} = %{version}-%{release}

%description swift
EmojiOne utility is for Swift.

%prep
%setup -q -c %{name}-%{version}
%patch1 -p1 -b .build
chmod a+x package/lib/python/emojipy/*.py
find . -name "*.js" -exec chmod 644 {} \;

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -R package/* %{buildroot}%{nodejs_sitelib}/%{module_name}
rm %{buildroot}%{nodejs_sitelib}/%{module_name}/CONTRIBUTING.md
rm %{buildroot}%{nodejs_sitelib}/%{module_name}/LICENSE.md
rm %{buildroot}%{nodejs_sitelib}/%{module_name}/README.md
rm %{buildroot}%{nodejs_sitelib}/%{module_name}/lib/tests.md
rm %{buildroot}%{nodejs_sitelib}/%{module_name}/lib/android/README.md
rm %{buildroot}%{nodejs_sitelib}/%{module_name}/lib/emojione-awesome/README.md
rm %{buildroot}%{nodejs_sitelib}/%{module_name}/lib/ios/README.md
rm %{buildroot}%{nodejs_sitelib}/%{module_name}/lib/python/README.md

# https://github.com/Ranks/emojione/issues/295
rm -rf %{buildroot}%{nodejs_sitelib}/%{module_name}/assets/fonts

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
grunt travis
%endif

%files
%license package/LICENSE.md
%doc package/CONTRIBUTING.md package/README.md package/lib/tests.md
%dir %{nodejs_sitelib}/%{module_name}/
%dir %{nodejs_sitelib}/%{module_name}/lib
%{nodejs_sitelib}/%{module_name}/lib/js
%{nodejs_sitelib}/%{module_name}/gruntfile.js
%{nodejs_sitelib}/%{module_name}/bower.json
%{nodejs_sitelib}/%{module_name}/assets

%files json
%license package/LICENSE.md
%{nodejs_sitelib}/%{module_name}/emoji*.json
%{nodejs_sitelib}/%{module_name}/package.js
%{nodejs_sitelib}/%{module_name}/package.json

%files android
%doc package/lib/android/README.md
%{nodejs_sitelib}/%{module_name}/lib/android

%files awesome
%doc package/lib/emojione-awesome/README.md
%{nodejs_sitelib}/%{module_name}/lib/emojione-awesome

%files meteor
%{nodejs_sitelib}/%{module_name}/lib/meteor

%files ios
%doc package/lib/ios/README.md
%{nodejs_sitelib}/%{module_name}/lib/ios

%files python
%doc package/lib/python/README.md
%{nodejs_sitelib}/%{module_name}/lib/python

%files swift
%doc package/lib/swift/README.md
%{nodejs_sitelib}/%{module_name}/lib/swift

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 20 2017 Takao Fujiwara <tfujiwar@redhat.com> - 2.2.7-3
- Move package.js* to json sub-package

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Takao Fujiwara <tfujiwar@redhat.com> - 2.2.7-1
- Bump to 2.2.7
- Add swift sub-package

* Fri Jul 22 2016 Takao Fujiwara <tfujiwar@redhat.com> - 2.2.6-3
- Subpackage for json files

* Fri Jul 22 2016 Takao Fujiwara <tfujiwar@redhat.com> - 2.2.6-1
- Initial implementation
