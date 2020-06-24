%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-ejs
Version:    1.0.0
Release:    12%{?dist}
Summary:    Embedded JavaScript templates for Node.js
# License text is included in Readme.md
License:    MIT
URL:        https://github.com/visionmedia/ejs
Source0:    http://registry.npmjs.org/ejs/-/ejs-%{version}.tgz

# Add patch to tests to bring up to a more modern 'should' syntax
Patch0:	    nodejs-ejs_fix-should-syntax.patch

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(should)
%endif

%description
%{summary}.


%prep
%setup -q -n package

%patch0 -p1


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ejs
cp -pr package.json ejs.js ejs.min.js index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/ejs

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha --require should --reporter spec
%endif


%files
%doc History.md Readme.md examples/
%{nodejs_sitelib}/ejs


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 25 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-4
- Fix test for newer should syntax

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.0
- update to upstream release 1.0.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.4-2
- restrict to compatible arches

* Wed May 29 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.4-1
- update to upstream release 0.8.4

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.3-1
- initial package
