%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-winston
Version:    0.7.3
Release:    13%{?dist}
Summary:    A multiple transport asynchronous logging library for Node.js
License:    MIT
URL:        https://github.com/flatiron/winston
Source0:    http://registry.npmjs.org/winston/-/winston-%{version}.tgz

Patch0:     %{name}-0.7.2-Remove-stream-tests.patch
Patch1:     %{name}-0.7.3-Shutdown-server.patch

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(async)
BuildRequires:  npm(colors)
BuildRequires:  npm(combined-stream)
BuildRequires:  npm(cycle)
BuildRequires:  npm(eyes)
BuildRequires:  npm(pkginfo)
BuildRequires:  npm(stack-trace)
BuildRequires:  npm(vows)
%endif

%description
This module is a multiple transport asynchronous logging library for Node.js.

Winston is designed to be a simple and universal logging library with support
for multiple transports. A transport is essentially a storage device for your
logs. Each instance of a winston logger can have multiple transports
configured at different levels. For example, one may want error logs to be
stored in a persistent remote location (like a database), but all logs output
to the console or a local file.

There also seemed to be a lot of logging libraries out there that coupled
their implementation of logging (ie, how the logs are stored/indexed) to the
API that they exposed to the programmer. This library aims to decouple those
parts of the process to make it more flexible and extensible.


%prep
%setup -q -n package
find . -type f -iname '*.js' -exec chmod -x '{}' \;
%patch0 -p1
%patch1 -p1
%nodejs_fixdep async '^1.5.0'
%nodejs_fixdep colors '^1.1.2'
%nodejs_fixdep request '^2.14'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/winston
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/winston

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
rm -f test/transports/webhook-test.js
%{nodejs_sitelib}/vows/bin/vows --spec --isolate
%endif


%files
%doc CHANGELOG.md LICENSE README.md docs/ examples/
%{nodejs_sitelib}/winston


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Tom Hughes <tom@compton.nu> - 0.7.3-10
- Update npm(request) dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.7.3-4
- Update npm(async) and npm(colors) dependencies
- Patch tests to avoid hang

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.3-2
- update to upstream release 0.7.3

* Tue Aug 20 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.2-3
- restrict to compatible arches

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 01 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.2-1
- update to upstream release 0.7.2
- fix spelling in %%summary

* Fri Jun 07 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.1-2
- remove execute bit from files that shouldn't have it

* Sun May 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.1-1
- update to upstream release 0.7.1

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.2-1
- initial package
