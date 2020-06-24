%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:           nodejs-grunt-contrib-uglify
Version:        0.11.1
Release:        12%{?dist}
Summary:        Minify files with UglifyJS
License:        MIT
URL:            https://github.com/gruntjs/grunt-contrib-uglify
Source0:        https://github.com/gruntjs/grunt-contrib-uglify/archive/v%{version}/grunt-contrib-uglify-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch:  %{nodejs_arches} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(chalk)
BuildRequires:  npm(lodash)
BuildRequires:  npm(maxmin)
BuildRequires:  npm(uglify-js)
BuildRequires:  npm(uri-path)
BuildRequires:  npm(grunt-cli)
BuildRequires:  npm(grunt-contrib-clean)
BuildRequires:  npm(grunt-contrib-internal)
BuildRequires:  npm(grunt-contrib-nodeunit)
%endif

%description
%{summary}.


%prep
%setup -q -n grunt-contrib-uglify-%{version}
%nodejs_fixdep lodash "^3.10.1"
%nodejs_fixdep maxmin "^2.1.0"
%nodejs_fixdep uglify-js ">=2.6.0"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-contrib-uglify
cp -pr package.json tasks/ \
    %{buildroot}%{nodejs_sitelib}/grunt-contrib-uglify
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/grunt uglify
/usr/bin/grunt nodeunit
%endif


%files
%doc README.md CONTRIBUTING.md AUTHORS CHANGELOG docs/
%license LICENSE-MIT
%{nodejs_sitelib}/grunt-contrib-uglify


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Troy Dawson <tdawson@redhat.com> - 0.11.1-8
- Update npm(uglify-js) dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Tom Hughes <tom@compton.nu> - 0.11.1-4
- Update npm(maxmin) dependency

* Mon Feb 22 2016 Tom Hughes <tom@compton.nu> - 0.11.1-3
- Remove npm(chalk) fixdep

* Sat Feb 13 2016 Tom Hughes <tom@compton.nu> - 0.11.1-2
- Update npm(chalk) dependency

* Thu Feb 11 2016 Tom Hughes <tom@compton.nu> - 0.11.1-1
- Update to 0.11.1 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Tom Hughes <tom@compton.nu> - 0.5.0-3
- Update npm(lodash) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.0-1
- update to upstream release 0.5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 08 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-3
- patch out use of maxmin where js-zlib cannot be packaged

* Wed Mar 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-2
- 'nodejs_fixdep uglify-js' required because our dependency handler doesn't yet
  support the package.json '^' notation

* Wed Mar 12 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-1
- update to upstream release 0.4.0

* Mon Feb 24 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.2-1
- update to upstream release 0.3.2

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.2-1
- initial package

