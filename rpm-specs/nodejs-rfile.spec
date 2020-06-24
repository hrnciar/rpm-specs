%{?nodejs_find_provides_and_requires}

%global packagename rfile
%global enable_tests 1

Name:		nodejs-rfile
Version:	1.0.0
Release:	6%{?dist}
Summary:	Require a plain text or binary file in node.js

License:	MIT
URL:		https://github.com/ForbesLindesay/rfile.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	https://raw.githubusercontent.com/ForbesLindesay/rfile/master/LICENSE


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	dos2unix
BuildRequires:	nodejs-packaging
BuildRequires:	npm(callsite)
BuildRequires:	npm(resolve)
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Require a plain text or binary file in node.js


%prep
%autosetup -n package
cp -p %{SOURCE1} .

%nodejs_fixdep resolve

dos2unix README.md

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
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
%license LICENSE
%{nodejs_sitelib}/%{packagename}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging
