Name:           fedora-repo-zdicts
Version:        2004.2
Release:        1%{?dist}
Summary:        Zstd dictionaries for Fedora repository metadata
License:        BSD
URL:            https://pagure.io/fedora-repo-zdicts
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  /bin/bash
 
%description
zchunk is a compressed file format that splits the file into independent
chunks.  This package contains zstd libraries tailored for Fedora's repository
metadata to improve their compression.


%prep
%autosetup


%build
# This package contains pregenerated zstd dictionaries so we don't have to
# carry 60+MB of metadata per Fedora release in the SRPM (and so we're not
# filling up our git repository)


%install
%make_install


%check


%files
%license LICENSE
%doc README.md
%{_datadir}/fedora-repo-zdicts

%changelog
* Sat Apr 04 2020 Jonathan Dieter <jdieter@gmail.com> - 2004.2-1
- Update with F32 dictionaries

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1910.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Jonathan Dieter <jdieter@gmail.com> - 1920.1-1
- Update with F31 dictionaries

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1812.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1812.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Jonathan Dieter <jdieter@gmail.com> - 1812.1-1
- Switch versioning to match yearmonth.release
- Fix paths to use koji tags

* Thu Dec 06 2018 Jonathan Dieter <jdieter@gmail.com> - 30.4-1
- Preserve timestamps

* Wed Dec 05 2018 Jonathan Dieter <jdieter@gmail.com> - 30.3-1
- Initial build of Fedora 30 repodata
