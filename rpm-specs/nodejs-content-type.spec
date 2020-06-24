%{?nodejs_find_provides_and_requires}

%global packagename content-type
%global enable_tests 1

Name:		nodejs-%{packagename}
Version:	1.0.4
Release:	6%{?dist}
Summary:	Create and parse HTTP Content-Type header according to RFC 7231

License:	MIT
URL:		https://github.com/jshttp/content-type
Source0:	https://github.com/jshttp/content-type/archive/v%{version}.tar.gz

ExclusiveArch:	%{nodejs_arches} noarch
BuildArch:	noarch

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	mocha
%endif

Requires:	nodejs

%description
Create and parse HTTP Content-Type header according to RFC 7231


%prep
%setup -q -n %{packagename}-%{version}


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
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 01 2017 Jared Smith <jsmith@fedoraproject.org> - 1.0.4-1
- Update to upstream 1.0.4 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jared Smith <jsmith@fedoraproject.org> - 1.0.2-1
- Update to upstream 1.0.2 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct  7 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.1-1
- Initial packaging
