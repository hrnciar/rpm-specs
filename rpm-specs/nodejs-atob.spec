%{?nodejs_find_provides_and_requires}

%global packagename atob
%global enable_tests 1

Name:		nodejs-atob
Version:	2.1.1
Release:	7%{?dist}
Summary:	An atob function for Node.JS and Linux / Mac / Windows CLI

License:	ASL 2.0 or MIT
URL:		https://github.com/coolaj86/node-browser-compat.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging

Requires:	nodejs

%description
Provides atob for Node.JS and Linux / Mac / Windows CLI (it's a one-liner)


%prep
%setup -q -n package

sed -i '1s/env //' bin/atob.js
chmod +x bin/atob.js


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json node-atob.js bin/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%__nodejs test.js
%{_bindir}/echo -e "\e[102m -=#=- Tests passed -=#=- \e[0m"
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE LICENSE.DOCS
%{nodejs_sitelib}/%{packagename}



%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 01 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2.1.1-1
- Update to upstream 2.1.1 release to address CVE-2018-3745

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Apr 14 2017 Jared Smith <jsmith@fedoraproject.org> - 2.0.3-1
- Update to upstream 2.0.3 release

* Sun Oct 25 2015 Jared Smith <jsmith@fedoraproject.org> - 1.1.2-2
- Rebuild to fix tests

* Fri Oct 23 2015 Jared Smith <jsmith@fedoraproject.org> - 1.1.2-1
- Initial packaging
