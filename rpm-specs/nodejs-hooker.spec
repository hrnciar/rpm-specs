%{?nodejs_find_provides_and_requires}

%global enable_tests 0

# This package requires the grunt stack, but grunt also requires this package.
# Before grunt is available, this will need to be built manually.
%global enable_grunt 0

Name:       nodejs-hooker
Version:    0.2.3
Release:    15%{?dist}
Summary:    Monkey-patch (hook) functions for debugging
License:    MIT
URL:        https://github.com/cowboy/javascript-hooker
Source0:    http://registry.npmjs.org/hooker/-/hooker-%{version}.tgz

# This is taken from the upstream version control repository.
Patch0:     %{name}-0.2.3-Updating-gruntfile-to-grunt-0.3.0-format.patch
# These two patches update grunt.js for use with grunt 0.4.0.
# Pull request sent: https://github.com/cowboy/javascript-hooker/pull/3
Patch1:     %{name}-0.2.3-Rename-grunt.js-to-Gruntfile.js.patch
Patch2:     %{name}-0.2.3-Update-Gruntfile.js-for-use-with-grunt-0.4.0.patch

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging
BuildRequires:  uglify-js

%if 0%{?enable_tests}
BuildRequires:  npm(nodeunit)
%endif

%if 0%{?enable_grunt}
BuildRequires:  npm(grunt-cli)
BuildRequires:  npm(grunt-contrib-nodeunit)
BuildRequires:  npm(grunt-contrib-uglify)
%endif

%description
%{summary}.


%prep
%setup -q -n package
%patch0 -p1
%patch1 -p1
%patch2 -p1
%nodejs_symlink_deps --check


%build
%if 0%{?enable_grunt}
grunt uglify
%else
# Add copyright header to the minified script.
head -n 8 lib/hooker.js > dist/ba-hooker.min.js.new
# Minify and preserve timestamp.
/usr/bin/uglifyjs dist/ba-hooker.js -m -c >> dist/ba-hooker.min.js.new
touch -r dist/ba-hooker.min.js dist/ba-hooker.min.js.new
mv dist/ba-hooker.min.js{.new,}
%endif


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/hooker
cp -pr package.json child.js dist/ lib/ parent.js \
    %{buildroot}%{nodejs_sitelib}/hooker

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%if 0%{?enable_grunt}
grunt nodeunit
%else
%{nodejs_sitelib}/nodeunit/bin/nodeunit test/*.js
%endif
%endif


%files
%doc LICENSE-MIT README.md
%{nodejs_sitelib}/hooker


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.3-4
- depend specifically on latest uglify-js

* Thu Jul 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.3-3
- disable tests until npm(nodeunit) is packaged

* Tue Jul 09 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.3-2
- add enable_grunt macro

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.3-1
- initial package
