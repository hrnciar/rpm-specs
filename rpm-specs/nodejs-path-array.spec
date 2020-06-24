%{?nodejs_find_provides_and_requires}

%global packagename path-array
%global enable_tests 1

Name:		nodejs-path-array
Version:	1.0.1
Release:	8%{?dist}
Summary:	Treat your $PATH like a JavaScript Array

License:	MIT
# License text is at the bottom of README.md
URL:		https://github.com/TooTallNate/node-path-array.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(array-index)
%endif

%description
Treat your $PATH like a JavaScript Array


%prep
%setup -q -n package

%nodejs_fixdep array-index '>=0.1.0'

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
%doc *.md
%license README.md
# license text is at the bottom of README.md, so I'm including it in both doc and
# license sections
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 12 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-1
- Update to upstream 1.0.1 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-2
- Relax dependency on npm(array-index)

* Wed Dec 16 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-1
- Initial packaging