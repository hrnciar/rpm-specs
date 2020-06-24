%{?nodejs_find_provides_and_requires}

# tests disabled due to missing npm(ava)
%global enable_tests 0

Name:       nodejs-pretty-bytes
Version:    4.0.2
Release:    7%{?dist}
Summary:    Convert bytes to a human readable string
License:    MIT
URL:        https://github.com/sindresorhus/pretty-bytes
Source0:    http://registry.npmjs.org/pretty-bytes/-/pretty-bytes-%{version}.tgz
Source1:    https://raw.githubusercontent.com/sindresorhus/pretty-bytes/v%{version}/test.js

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(ava)
%endif

%description
%{summary}.


%prep
%setup -q -n package
cp -p %{SOURCE1} .


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/pretty-bytes
cp -pr package.json *.js \
    %{buildroot}%{nodejs_sitelib}/pretty-bytes

mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/pretty-bytes/cli.js \
    %{buildroot}%{_bindir}/pretty-bytes

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/ava
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%license license
%doc readme.md
%{nodejs_sitelib}/pretty-bytes
%{_bindir}/pretty-bytes


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jared Smith <jsmith@fedoraproject.org> - 4.0.2-2
- Remove unneeded dependency on npm(number-is-nan)

* Fri Sep 22 2017 Jared Smith <jsmith@fedoraproject.org> - 4.0.2-1
- Update to upstream 4.0.2 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 08 2016 Jared Smith <jsmith@fedoraproject.org> - 3.0.1-1
- Update to upstream 3.0.1 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.0-1
- initial package
