# test dependency not yet in Fedora
%global enable_tests 0
%global srcname formatio

Name:           nodejs-%{srcname}
Version:        1.2.0
Release:        8%{?dist}
Summary:        Human-readable object formatting
License:        BSD
URL:            https://github.com/busterjs/formatio
Source0:        https://registry.npmjs.org/%{srcname}/-/%{srcname}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  nodejs-samsam

%if 0%{?enable_tests}
BuildRequires:  npm(buster)
%endif

%description
Pretty formatting of arbitrary JavaScript values. Currently only supports 
ascii formatting, suitable for command-line utilities. Like JSON.stringify, it 
formats objects recursively, but unlike JSON.stringify, it can handle regular 
expressions, functions, circular objects and more.

formatio is a general-purpose library. It works in browsers (including old and 
rowdy ones, like IE6) and Node. It will define itself as an AMD module if you 
want it to (i.e. if there's a define function available).

%prep
%autosetup -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{srcname}
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/%{srcname}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{__nodejs} node_modules/buster/bin/buster-test --node
%endif

%files
%doc AUTHORS Readme.md
%license LICENSE
%{nodejs_sitelib}/%{srcname}


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 18 2017 Piotr Popieluch <piotr1212@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 16 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.1.3-1
- Update to 1.1.3

* Fri Jan 02 2015 Piotr Popieluch <piotr1212@gmail.com> - 1.1.2-1
- updated to latest upstream

* Tue Nov 18 2014 Piotr Popieluch <piotr1212@gmail.com> - 1.1.1-1
- Initial package
