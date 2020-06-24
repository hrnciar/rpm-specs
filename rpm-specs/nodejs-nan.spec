%global npm_name nan

%{?nodejs_find_provides_and_requires}

Summary:       Native Abstractions for Node.js 
Name:          nodejs-%{npm_name}
Version:       2.14.1
Release:       1%{?dist}
License:       MIT
URL:           https://github.com/nodejs/nan
Source0:       https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs-packaging
BuildArch:     noarch
ExclusiveArch: %{nodejs_arches} noarch

# nan is a header only library statically included by dependents
Provides:      nodejs-nan-devel = %{version}-%{release}
Provides:      nodejs-nan-static = %{version}-%{release}

%description
A header file filled with macro and utility goodness
for making add on development for Node.js easier across
versions 0.8, 0.10 and 0.11, and eventually 0.12.

Thanks to the crazy changes in V8 (and some in Node core),
keeping native add-on compiling happily across versions,
particularly 0.10 to 0.11/0.12, is a minor nightmare. 
The goal of this project is to store all logic necessary
to develop native Node.js add-on without having to inspect 
NODE_MODULE_VERSION and get yourself into a macro-tangle.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}@2
cp -pr include_dirs.js nan*.h package.json  %{buildroot}%{nodejs_sitelib}/%{npm_name}@2

ln -sf nan@2 %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%doc CHANGELOG.md README.md doc
%license LICENSE.md
%{nodejs_sitelib}/%{npm_name}
%{nodejs_sitelib}/%{npm_name}@2

%pretrans -p <lua>
-- Define the path to directory being replaced below.
-- DO NOT add a trailing slash at the end.
path = "%{nodejs_sitelib}/%{npm_name}"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

%changelog
* Tue Apr 21 2020 Tom Hughes <tom@compton.nu> - 2.14.1-1
- Update to 2.14.1 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 16 2019 Tom Hughes <tom@compton.nu> - 2.14.0-1
- Update to 2.14.0 upstream release

* Sun Mar 24 2019 Tom Hughes <tom@compton.nu> - 2.13.2-1
- Update to 2.13.2 upstream release

* Fri Mar 15 2019 Tom Hughes <tom@compton.nu> - 2.13.1-1
- Update to 2.13.1 upstream release

* Thu Mar 14 2019 Tom Hughes <tom@compton.nu> - 2.13.0-1
- Update to 2.13.0 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 17 2018 Tom Hughes <tom@compton.nu> - 2.10.0-1
- Update to 2.10.0 upstream release

* Fri Feb 23 2018 Tom Hughes <tom@compton.nu> - 2.9.2-1
- Update to 2.9.2 upstream release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 Tom Hughes <tom@compton.nu> - 2.8.0-1
- Update to 2.8.0 upstream release

* Wed Aug 30 2017 Tom Hughes <tom@compton.nu> - 2.7.0-1
- Update to 2.7.0 upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 13 2017 Tom Hughes <tom@compton.nu> - 2.6.2-1
- Update to 2.6.2 upstream release

* Thu Apr  6 2017 Tom Hughes <tom@compton.nu> - 2.6.1-1
- Update to 2.6.1 upstream release

* Thu Apr  6 2017 Tom Hughes <tom@compton.nu> - 2.6.0-1
- Update to 2.6.0 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Tom Hughes <tom@compton.nu> - 2.5.1-1
- Update to 2.5.1 upstream release

* Thu Dec 22 2016 Tom Hughes <tom@compton.nu> - 2.5.0-1
- Update to 2.5.0 upstream release

* Mon Jul 11 2016 Tom Hughes <tom@compton.nu> - 2.4.0-1
- Update to 2.4.0 upstream release

* Thu Jun 16 2016 Tom Hughes <tom@compton.nu> - 2.3.5-1
- Update to 2.3.5 upstream release

* Mon May 16 2016 Tom Hughes <tom@compton.nu> - 2.3.3-1
- Update to 2.3.3 upstream release

* Wed Apr 27 2016 Tom Hughes <tom@compton.nu> - 2.3.2-1
- Update to 2.3.2 upstream release

* Wed Mar 30 2016 Tom Hughes <tom@compton.nu> - 2.2.1-1
- Update to 2.2.1 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Tom Hughes <tom@compton.nu> - 2.2.0-1
- Update to 2.2.0 upstream release

* Mon Nov 23 2015 Tom Hughes <tom@compton.nu> - 2.1.0-1
- Update to 2.1.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 05 2015 Troy Dawson <tdawson@redhat.com> - 1.8.4-1
- Updated to latest release

* Wed Feb 25 2015 Troy Dawson <tdawson@redhat.com> - 1.6.2-1
- Updated to latest release

* Fri Jan 23 2015 Troy Dawson <tdawson@redhat.com> - 1.6.1-1
- Updated to latest release

* Thu Jan 22 2015 Troy Dawson <tdawson@redhat.com> - 1.5.1-1
- Updated to latest release

* Fri Oct 24 2014 Troy Dawson <tdawson@redhat.com> - 1.3.0-1
- Updated to latest release

* Mon Jun 09 2014 Troy Dawson <tdawson@redhat.com> - 1.2.0-2
- Fix the co-existance link

* Mon Jun 09 2014 Troy Dawson <tdawson@redhat.com> - 1.2.0-1
- Update to version 1.2.0

* Sun May 25 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-2
- support coexistence with nodejs-nan0
- comply with the header only library policy

* Fri May 09 2014 Troy Dawson <tdawson@redhat.com> - 1.0.0-1
- Update to version 1.0.0

* Thu Feb 06 2014 Troy Dawson <tdawson@redhat.com> - 0.8.0-1
- Update to version 0.8.0
- add nodejs exclusive arch
- add macro to invoke dependency generator on EL6

* Fri Nov 08 2013 Troy Dawson <tdawson@redhat.com> - 0.4.4-1
- Update to 0.4.4

* Mon Oct 07 2013 Troy Dawson <tdawson@redhat.com> - 0.4.1-1
- Initial build
