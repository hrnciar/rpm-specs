Summary: Calculates distance and azimuth between two Maidenhead locators
Name: wwl
Version: 1.3
Release: 2%{?dist}
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/SVSSA3AYDGFHA4NZWJPZCNNBRSSUV5DT/
License: Semi-Permissive
URL: http://www.db.net/downloads/
Source: http://www.db.net/downloads/wwl+db-%{version}.tgz
BuildRequires: gcc
BuildRequires: make

%description
This program combines two handy ham radio Maindensquare programs into one.
When used as locator, it will take the Maindenhead square on the
command line and write it back out as lat / long.
When used as wwl, it will calculate distance and azimuth
between the two Maidenhead squares given.
If only four characters of the Maidenhead square is given, this
program will auto fill in the missing two chars with 'AA'.

%prep
%autosetup -n wwl+db-%{version}

%build
%make_build CFLAGS="%{optflags}"

%install
mkdir -p "%{buildroot}%{_bindir}" "%{buildroot}%{_mandir}/man1"
%make_install PREFIX="%{buildroot}%{_prefix}" MAN1PREFIX="%{buildroot}%{_mandir}/man1/" LN="ln -r"
chmod 0644 %{buildroot}%{_mandir}/man1/wwl.1*

%files
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Thu Oct  1 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.3-2
- Fixed according to the review

* Thu Aug 20 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.3-1
- Initial release
