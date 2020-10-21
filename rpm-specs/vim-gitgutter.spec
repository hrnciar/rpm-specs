%global commit  b356cc9a7da08ebeb919cd04b2831dad71a34d38
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20200501

Name:           vim-gitgutter
Version:        0
Release:        5.%{date}git%{shortcommit}%{?dist}
Summary:        Shows a git diff in the gutter and stages/undoes hunks and partial hunks

License:        MIT
URL:            https://github.com/airblade/vim-gitgutter
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml
BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem

Requires:       vim-enhanced

%description
A Vim plugin which shows a git diff in the 'gutter' (sign column). It shows
which lines have been added, modified, or removed. You can also preview, stage,
and undo individual hunks; and stage partial hunks. The plugin also provides a
hunk text object.

The signs are always up to date and the plugin never saves your buffer.


%prep
%autosetup -n %{name}-%{commit} -p1


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -rp {autoload,plugin,unplace.vim} %{buildroot}%{vimfiles_root}
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENCE
%doc README.mkd doc/* test
%{vimfiles_root}/autoload/*
%{vimfiles_root}/plugin/*
%{vimfiles_root}/unplace.vim
%{_metainfodir}/*.xml


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-5.20200501gitb356cc9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-4.20200501gitb356cc9
- Update to latest git snapshot

* Sat Mar 28 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-3.20200328git7c48aa1
- Update to latest git snapshot

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-3.20191207git1c53af9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-2.20191207git1c53af9
- Update to latest git snapshot

* Thu Oct 17 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-2.20191015git5c73edb
- Update to latest git snapshot

* Thu Oct 03 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20191001git1725c13
- Initial package
