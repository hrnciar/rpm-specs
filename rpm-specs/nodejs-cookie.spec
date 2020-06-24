%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-cookie
Version:    0.3.1
Release:    6%{?dist}
Summary:    Cookie parsing and serialization for Node.js
License:    MIT
URL:        https://github.com/shtylman/node-cookie
Source0:    http://registry.npmjs.org/cookie/-/cookie-%{version}.tgz
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:    tests-%{version}.tar.bz2
Source10:   dl-tests.sh


BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
%endif

%description
This Node.js module is a basic cookie parser and serializer. It doesn't
make assumptions about how you are going to deal with your cookies. It
basically just provides a way to read and write the HTTP cookie headers.

See RFC6265 for details about the HTTP header for cookies.


%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/cookie
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/cookie

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/cookie


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Jared Smith <jsmith@fedoraproject.org> - 0.3.1-1
- Update to upstream 0.3.1 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.2-1
- update to upstream release 0.1.2

* Sat Mar 08 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.1-1
- update to upstream release 0.1.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-3
- fix compatible arches for f18/el6

* Fri Jul 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-2
- restrict to compatible arches

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-1
- update to upstream release 0.1.0

* Tue Apr 09 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.6-1
- update to upstream release 0.0.6
- enable %%check
- add LICENSE

* Tue Feb 12 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.5-2
- correct capitalization in the description

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.0.5-1
- initial package
