%{?nodejs_find_provides_and_requires}

%global packagename http-errors
%global enable_tests 1

Name:		nodejs-http-errors
Version:	1.7.3
Release:	1%{?dist}
Summary:	Create HTTP errors for Express, Koa, Connect, etc. with ease

License:	MIT
URL:		https://github.com/jshttp/http-errors
Source0:	https://github.com/jshttp/http-errors/archive/%{version}.tar.gz


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif


BuildRequires:	nodejs-packaging
BuildRequires:	npm(statuses)
BuildRequires:	npm(inherits)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(depd)
BuildRequires:	npm(setprototypeof)
BuildRequires:  npm(toidentifier)
%endif

Requires:	nodejs

%description
Create HTTP errors for Express, Koa, Connect, etc. with ease

%prep
%setup -q -n %{packagename}-%{version}
%nodejs_fixdep inherits "^2.0.1"
%nodejs_fixdep --caret setprototypeof


%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
/usr/bin/mocha -R spec
%endif


%files
%{!?_licensedir:%global license %doc}
%doc README.md HISTORY.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Feb 19 2020 Ben Rosser <rosser.bjr@gmail.com> - 1.7.3-1
- Update to latest upstream version, 1.7.3.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Jared Smith <jsmith@fedoraproject.org> - 1.6.2-1
- Update to upstream 1.6.2 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 1.4.0-4
- Update npm(inherits) dependency

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Jared Smith <jsmith@fedoraproject.org> - 1.4.0-1
- Update to upstream 1.4.0 release

* Mon Nov 02 2015 Jared Smith <jsmith@fedoraproject.org> - 1.3.1-2
- Fix ExclusiveArch for building on EPEL

* Wed Oct  7 2015 Jared Smith <jsmith@fedoraproject.org> - 1.3.1-1
- Initial packaging
