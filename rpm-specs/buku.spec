Name:       buku
Version:    4.4
Release:    1%{?dist}
Summary:    Powerful command-line bookmark manager

License:    GPLv3+
URL:        https://github.com/jarun/Buku
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  make
Requires:       %{py3_dist beautifulsoup4 certifi urllib3 cryptography html5lib}


%description
buku is a powerful bookmark manager written in Python3 and SQLite3.

buku fetches the title of a bookmarked web page and stores it along
with any additional comments and tags. You can use your favourite editor
to compose and update bookmarks. With multiple search options, including regex
and a deep scan mode (particularly for URLs), it can find any bookmark
instantly. Multiple search results can be opened in the browser at once.


%prep
%autosetup -p1
sed -i '1s/env //' buku


%build
# Nothing to do


%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  auto-completion/bash/buku-completion.bash
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_functions.d \
  auto-completion/fish/buku.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions \
  auto-completion/zsh/_buku


%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/bash-completion/completions/buku-completion.bash
%dir %{_datadir}/fish/vendor_functions.d
%{_datadir}/fish/vendor_functions.d/buku.fish
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_buku


%changelog
* Wed Jun 17 14:47:38 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 4.4-1
- Update to 4.4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 02 11:22:11 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 4.2.2-1
- Release 4.2.2

* Tue Apr 30 15:23:59 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 4.2-1
- Release 4.2

* Sat Mar 09 2019 Robert-André Mauchin <zebob.m@gmail.com> - 4.1-1
- Release 4.1

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Robert-André Mauchin <zebob.m@gmail.com> - 4.0-2
- Add missing Requires

* Thu Nov 01 2018 Robert-André Mauchin <zebob.m@gmail.com> - 4.0-1
- Release 4.0

* Thu Aug 30 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.9-1
- Release 3.9

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.8-1
- Release 3.8

* Wed Mar 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.7-1
- Release 3.7

* Sat Feb 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 3.6-1
- First RPM release
