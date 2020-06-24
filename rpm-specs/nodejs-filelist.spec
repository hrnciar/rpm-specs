Name:           nodejs-filelist
Version:        0.0.6
Release:        8%{?dist}
Summary:        Lazy-evaluating list of files, based on globs or regexes

License:        ASL 2.0
URL:            https://github.com/mde/filelist
Source0:        https://github.com/mde/filelist/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(jake)
BuildRequires:  npm(utilities)

%description
A FileList is a lazy-evaluated list of files. When given a list of
glob patterns for possible files to be included in the file list,
instead of searching the file structures to find the files, a FileList
holds the pattern for latter use.

This allows you to define a FileList to match any number of files, but
only search out the actual files when then FileList itself is actually
used. The key is that the first time an element of the FileList/Array
is requested, the pending patterns are resolved into a real list of
file names.


%prep
%setup -q -n filelist-%{version}
%nodejs_fixdep minimatch "^3.0.0"
%nodejs_fixdep utilities "^1.0.4"
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/filelist
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/filelist
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
jake test


%files
%doc LICENSE README.md
%{nodejs_sitelib}/filelist


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Tom Hughes <tom@compton.nu> - 0.0.6-1
- Update to 0.0.6 upstream release

* Wed Nov 30 2016 Tom Hughes <tom@compton.nu> - 0.0.5-1
- Update to 0.0.5 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 0.0.4-2
- Update minimatch dependency

* Wed Aug 26 2015 Tom Hughes <tom@compton.nu> - 0.0.4-1
- Update to 0.0.4 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 Tom Hughes <tom@compton.nu> - 0.0.3-2
- Enable tests

* Sat Nov 15 2014 Tom Hughes <tom@compton.nu> - 0.0.3-1
- Initial build of 0.0.3
