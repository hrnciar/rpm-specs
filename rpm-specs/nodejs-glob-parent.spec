%{?nodejs_find_provides_and_requires}

%global packagename glob-parent

# tests disabled due to failing tests because of npm(is-glob) 4.0.0
%global enable_tests 0

Name:		nodejs-glob-parent
Version:	3.1.0
Release:	7%{?dist}
Summary:	Strips glob magic from a string to provide the parent path

License:	ISC
URL:		https://github.com/es128/glob-parent
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
# test is not in npm module
Source1:	https://raw.githubusercontent.com/es128/glob-parent/v%{version}/test.js

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	npm(is-glob)
BuildRequires:	npm(path-dirname)
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

%description
Strips glob magic from a string to provide the parent path


%prep
%setup -q -n package
cp -p %{SOURCE1} .

%nodejs_fixdep is-glob

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
%{_bindir}/echo "Tests disabled..."
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Jared Smith <jsmith@fedoraproject.org> - 3.1.0-1
- Update to upstream 3.1.0 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-2
- Add missing BuildRequire line

* Tue Feb  9 2016 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Initial packaging
