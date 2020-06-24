%{?nodejs_find_provides_and_requires}

# These tests are interactive so cannot be run in mock.
# Also, I'm not sure why they are failing outside of mock too.
%global enable_tests 0

Name:       nodejs-prompt
Version:    0.2.14
Release:    10%{?dist}
Summary:    A beautiful command-line prompt for Node.js
License:    MIT
URL:        https://github.com/flatiron/prompt
Source0:    https://registry.npmjs.org/prompt/-/prompt-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(read)
BuildRequires:  npm(revalidator)
BuildRequires:  npm(utile)
BuildRequires:  npm(vows)
BuildRequires:  npm(winston)
%endif

%description
A beautiful command-line prompt for Node.js. Features include:
 - prompting for user input
 - validation and defaults
 - hiding of passwords


%prep
%setup -q -n package
%nodejs_fixdep utile '^0.3.0'
%nodejs_fixdep winston '~0.7'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/prompt
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/prompt

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{nodejs_sitelib}/vows/bin/vows --spec
%endif


%files
%doc CHANGELOG.md README.md docs/ examples/
%license LICENSE
%{nodejs_sitelib}/prompt


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Tom Hughes <tom@compton.nu> - 0.2.14-7
- Update npm(winston) dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.2.14-1
- Update to 0.2.14 upstream release
- Update npm(utile) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.12-1
- update to upstream release 0.2.12

* Tue Sep 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.11-1
- update to upstream release 0.2.11

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.9-2
- make some of the versioned dependencies less specific

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.9-1
- initial package
