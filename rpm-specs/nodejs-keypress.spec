%{?nodejs_find_provides_and_requires}

# test.js does not like being run in mock (ie, non-tty)
%global enable_tests 0

Name:       nodejs-keypress
Version:    0.2.1
Release:    11%{?dist}
Summary:    Make any Node ReadableStream emit "keypress" events
# License text is included in README.md
License:    MIT
URL:        https://github.com/TooTallNate/keypress
Source0:    http://registry.npmjs.org/keypress/-/keypress-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
Previous to Node v0.8.x, there was an undocumented "keypress" event that
process.stdin would emit when it was a TTY. Some people discovered this
hidden gem, and started using it in their own code.

In Node v0.8.x, this "keypress" event does not get emitted by default,
but rather only when it is being used in conjunction with the readline
(or by extension, the repl) module.

This module is the exact logic from the node v0.8.x releases ripped out
into its own module.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/keypress
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/keypress

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%__nodejs test.js
%endif


%files
%doc README.md
%{nodejs_sitelib}/keypress


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.1-1
- update to upstream release 0.2.1

* Sat Jul 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-4
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-3
- rebuild for missing npm(keypress) provides on EL6

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-2
- fix a typo in the description

* Tue Feb 12 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-1
- initial package
