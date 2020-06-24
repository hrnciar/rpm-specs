%{?nodejs_find_provides_and_requires}

%global enable_tests 0
# tests failing

Name:       nodejs-ncp
Version:    2.0.0
Release:    8%{?dist}
Summary:    Asynchronous recursive file copy utility for Node.js
License:    MIT
URL:        https://github.com/AvianFlu/ncp
Source0:    http://registry.npmjs.org/ncp/-/ncp-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(deep-equal)
BuildRequires:  npm(mocha)
BuildRequires:  npm(read-dir-files)
BuildRequires:  npm(rimraf)
%endif

%description
This module is an asynchronous recursive copy utility for Node.js.
Think cp -r, but pure node, and asynchronous. ncp can be used both
as a CLI tool and programmatically.


%prep
%setup -q -n package

# fix interpreter
sed -i '1s/env //' bin/ncp

%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/ncp
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/ncp
mkdir -p %{buildroot}%{nodejs_sitelib}/ncp/bin
install -p -D -m0755 bin/ncp %{buildroot}%{nodejs_sitelib}/ncp/bin/ncp
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/ncp/bin/ncp %{buildroot}%{_bindir}/ncp

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
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE.md
%{nodejs_sitelib}/ncp
%{_bindir}/ncp


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Update to upstream 2.0.0 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.1-1
- update to upstream release 0.5.1

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.0-1
- update to upstream release 0.5.0

* Sun Jul 28 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.2-2
- restrict to compatible arches

* Sat May 25 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.2-1
- update to upstream release 0.4.2

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.0-1
- initial package
