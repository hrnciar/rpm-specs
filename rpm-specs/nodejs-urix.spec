%{?nodejs_find_provides_and_requires}

%global packagename urix
%global enable_tests 1

Name:		nodejs-urix
Version:	0.1.0
Release:	9%{?dist}
Summary:	Makes Windows-style paths more unix and URI friendly

License:	MIT
URL:		https://github.com/lydell/urix
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	dos2unix
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

Requires:	nodejs

%description
Makes Windows-style paths more unix and URI friendly.


%prep
%setup -q -n package

dos2unix readme.md

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
/usr/bin/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 28 2015 Jared Smith <jsmith@fedoraproject.org> - 0.1.0-4
- Re-enable tests

* Sun Oct 25 2015 Jared Smith <jsmith@fedoraproject.org> - 0.1.0-3
- Temporarily disabling tests until we can bootstrap newer npm(jade)

* Sun Oct 25 2015 Jared Smith <jsmith@fedoraproject.org> - 0.1.0-2
- Rebuild to fix build requirements

* Fri Oct 23 2015 Jared Smith <jsmith@fedoraproject.org> - 0.1.0-1
- Initial packaging