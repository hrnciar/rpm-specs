%{?nodejs_find_provides_and_requires}
%global enable_tests 1

Name:       nodejs-line-reader
Version:    0.4.0
Release:    10%{?dist}
Summary:    Asynchronous line-by-line file reader
License:    MIT
URL:        https://github.com/nickewing/line-reader
Source:     http://registry.npmjs.org/line-reader/-/line-reader-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
%endif

%description
Nodejs line reader is asynchronous line-by-line file reader

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/line-reader
cp -rp package.json lib/ %{buildroot}%{nodejs_sitelib}/line-reader

%check
%if 0%{?enable_tests}
mocha test/line_reader.js
%endif

%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/line-reader


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Anish Patil <anish.developer@gmail.com> - 0.4.0-1
- Upstream has released new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.2.4-3
- Move LICENSE to %%license
- Excluded tests from %%doc
- Renamed binary to line-reader instead of nodejs-line-reader
- Enabled tests
- Add ExclusiveArch for nodejs packages

* Thu Feb 26 2015 Anish Patil <apatil@redhat.com> - 0.2.4-2
- Added nodejs packaging dependencies

* Thu Feb 5 2015 Anish Patil <apatil@redhat.com> - 0.2.4-1
- initial package
