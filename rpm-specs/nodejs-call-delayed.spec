%{?nodejs_find_provides_and_requires}

%global packagename call-delayed
%global enable_tests 1

Name:		nodejs-call-delayed
Version:	1.0.0
Release:	7%{?dist}
Summary:	Like setTimeout, but with arguments reversed

License:	MIT
URL:		https://github.com/braveg1rl/call-delayed
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(bluebird)
BuildRequires:	npm(chai)
BuildRequires:	npm(coffee-script)
%endif

%description
setTimeout, but with arguments reversed.


%prep
%autosetup -n package

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

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
%license license.txt
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-2
- Add missing BuildRequires line for npm(coffee-script)

* Thu Dec 14 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
