Name:           rifiuti2
Version:        0.7.0
Release:        3%{?dist}
Summary:        A Windows Recycle Bin analyser

License:        BSD
URL:            https://github.com/abelcheung/rifiuti2
Source0:        https://github.com/abelcheung/rifiuti2/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gettext

%description
Rifiuti2 is a for analyzing Windows Recycle Bin INFO2 file. Analysis of
Windows Recycle Bin is usually carried out during Windows computer forensics.
Rifiuti2 can extract file deletion time, original path and size of deleted
files and whether the trashed files have been permanently removed.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}

%check
make check

%files -f %{name}.lang
%doc ChangeLog NEWS.md README.md docs/AUTHORS docs/THANKS
%license docs/LICENSE.md
%{_mandir}/man1/rifiuti*.*
%{_bindir}/rifiuti*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Initial package for Fedora
