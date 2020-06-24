%{?nodejs_find_provides_and_requires}

%global packagename sinon-restore
%global enable_tests 0

Name:		nodejs-sinon-restore
Version:	1.0.1
Release:	9%{?dist}
Summary:	Simply adds restoreAll() to sinon

License:	MIT
URL:		https://github.com/cainus/sinon-restore.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# License file requested upstream at https://github.com/cainus/sinon-restore/issues/2
Source1:	LICENSE-MIT.txt


ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
BuildRequires:	npm(sinon)
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

Requires:	nodejs

%description
Simply adds restoreAll() to sinon


%prep
%setup -q -n package
cp -p %{SOURCE1} .

%nodejs_fixdep sinon


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
# nothing to do
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE-MIT.txt
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 13 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-2
- Rebuilt to better adhere to packaging guidelines

* Thu Oct 15 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-1
- Initial packaging
