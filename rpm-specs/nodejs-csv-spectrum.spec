%{?nodejs_find_provides_and_requires}

%global packagename csv-spectrum
%global enable_tests 1

Name:		nodejs-csv-spectrum
Version:	1.0.0
Release:	9%{?dist}
Summary:	Some csv test data for writing robust csv parsers

License:	BSD
# License file requested at https://github.com/maxogden/csv-spectrum/issues/17
URL:		https://github.com/maxogden/csv-spectrum.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz

Source1:	LICENSE
# include the license until upstream adds it themselves

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
#BuildRequires:
%endif

Requires:	nodejs

%description
A collection of csv test data for writing robust csv parsers


%prep
%setup -q -n package
cp -p %{SOURCE1} .

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js json/ csvs/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__nodejs test.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov  8 2015 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-2
- Initial packaging