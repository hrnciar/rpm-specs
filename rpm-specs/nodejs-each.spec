%{?nodejs_find_provides_and_requires}

%global packagename each
%global enable_tests 0

Name:		nodejs-each
Version:	0.6.1
Release:	10%{?dist}
Summary:	Chained and parallel async iterator in one elegant function

License:	BSD
URL:		https://github.com/wdavidw/node-each.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
BuildRequires:	coffee-script

%if 0%{?enable_tests}
BuildRequires:	mocha
BuildRequires:	npm(should)
%endif

%description
Chained and parallel async iterator in one elegant function


%prep
%setup -q -n package

# remove pre-compiled script
rm lib/*.js

%nodejs_fixdep glob "^6.0.0"


%build
%{_bindir}/coffee -c -b -o lib/ src/

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js lib/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
NODE_ENV=test %{_bindir}/mocha --compilers coffee:coffee-script/register -R spec
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md samples/ doc/
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 04 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.1-2
- Add fixdep to npm(glob) dependency

* Sun Jul 03 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.1-1
- Update to upstream 0.6.1 release

* Wed Nov 11 2015 Jared Smith <jsmith@fedoraproject.org> - 0.5.2-4
- Increase timeout for mocha in tests

* Sun Nov 08 2015 Jared Smith <jsmith@fedoraproject.org> - 0.5.2-2
- Try working around a problem in coffee-script packaging

* Sun Nov  8 2015 Jared Smith <jsmith@fedoraproject.org> - 0.5.2-1
- Initial packaging
