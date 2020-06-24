%global commit  61d877d23caaad9009d672f90fe2ab576ab93d2d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20200522

Name:           vim-gv
Version:        0
Release:        5.%{date}git%{shortcommit}%{?dist}
Summary:        Git commit browser in Vim

License:        MIT
URL:            https://github.com/junegunn/gv.vim
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml
BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem

Requires:       vim-enhanced
Requires:       vim-fugitive

%description
A git commit browser.


%prep
%autosetup -n gv.vim-%{commit} -p1


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -rp plugin %{buildroot}%{vimfiles_root}
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%doc README.md test/
%{vimfiles_root}/plugin/*
%{_metainfodir}/*.xml


%changelog
* Sat May 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-5.20200522git61d877d
- Update to latest git snapshot

* Sat Mar 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-4.20200328git72dc64d
- Update to latest git snapshot

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20191207gitf12b8b8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-3.20191207gitf12b8b8
- Update to latest git snapshot
- Fix license

* Thu Oct 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-2.20191013git7a84f63
- Update to latest git snapshot

* Thu Oct 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20190911git0868f29
- Initial package
