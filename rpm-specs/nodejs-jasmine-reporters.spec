%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-jasmine-reporters
Version:    0.4.1
Release:    11%{?dist}
Summary:    Reporters for the Jasmine behavior-driven development (BDD) framework
License:    MIT
URL:        https://github.com/larrymyers/jasmine-reporters
Source0:    http://registry.npmjs.org/jasmine-reporters/-/jasmine-reporters-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(jasmine-node)
%endif

%description
%{summary}


%prep
%setup -q -n package
rm -rf ext/


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/jasmine-reporters
cp -pr package.json src/ \
    %{buildroot}%{nodejs_sitelib}/jasmine-reporters

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
/usr/bin/jasmine-node test/
%endif


%files
%doc LICENSE README.markdown
%{nodejs_sitelib}/jasmine-reporters


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.1-1
- update to upstream release 0.4.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-4
- restrict to compatible arches
- enable tests

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.1-3
- rebuild for missing npm(jasmine-reporters) provides on EL6

* Fri Mar 08 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-2
- remove bundled libraries in ext/
- add %%check section
- add npm(jasmine-node) to BuildRequires
- remove npm(phantomjs) from BuildRequires

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-1
- initial package
