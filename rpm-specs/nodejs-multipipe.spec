%{?nodejs_find_provides_and_requires}

%global packagename multipipe
%global enable_tests 1

Name:		nodejs-multipipe
Version:	1.0.2
Release:	6%{?dist}
Summary:	Pipe streams with centralized error handling

License:	MIT
URL:		https://github.com/juliangruber/multipipe.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(duplexer2)
BuildRequires:	npm(object-assign)
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(through2)
%endif

%description
Pipe streams with centralized error handling.


%prep
%setup -q -n package

# create license file from the Readme.md file

sed '0,/^## License/d' Readme.md > LICENSE.md

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
%{_bindir}/mocha -R spec
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"

%endif


%files
%{!?_licensedir:%global license %doc}
%doc Readme.md History.md
%license LICENSE.md
%{nodejs_sitelib}/%{packagename}


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Apr 19 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.2-1
- Update to upstream 1.0.2 release

* Fri Jul 15 2016 Jared Smith <jsmith@fedoraproject.org> - 0.3.1-1
- Update to upstream 0.3.1 release

* Mon Feb 22 2016 Jared Smith <jsmith@fedoraproject.org> - 0.3.0-1
- Initial packaging
