Name:           nodejs-resumer
Version:        0.0.0
Release:        10%{?dist}
Summary:        A stream that starts paused and resumes on the next tick

License:        MIT
URL:            https://github.com/substack/resumer
Source0:        http://registry.npmjs.org/resumer/-/resumer-%{version}.tgz
# https://github.com/substack/resumer/pull/2
Patch0:         nodejs-resumer-concat-stream.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(tap)
BuildRequires:  npm(tape)
BuildRequires:  npm(concat-stream)
BuildRequires:  npm(through)

%description
A through stream that starts paused and resumes on the next tick.


%prep
%setup -q -n package
%patch0 -p1
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/resumer
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/resumer
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%tap test/*.js


%files
%doc LICENSE readme.markdown example
%{nodejs_sitelib}/resumer


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 24 2014 Tom Hughes <tom@compton.nu> - 0.0.0-1
- Initial build of 0.0.0
