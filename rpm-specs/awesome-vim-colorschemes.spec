%global commit      b5037cbf87ee4b0beed91adb33c339122e58326f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191209

Name:           awesome-vim-colorschemes
Version:        0
Release:        9.%{date}git%{shortcommit}%{?dist}
Summary:        Collection of color schemes for Neo/vim, merged for quick use

# You can find the individual license in the actual vim file, or find the
# appropriate README in docs/
# * https://github.com/rafi/awesome-vim-colorschemes/issues/12
License:        Vim and MIT and CC-BY

URL:            https://github.com/rafi/awesome-vim-colorschemes
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        %{name}.metainfo.xml

# Remove executable bit & Fix wrong file end of line encoding
# * https://github.com/rafi/awesome-vim-colorschemes/pull/13
Patch0:         https://github.com/rafi/awesome-vim-colorschemes/pull/13#/remove-executable-bit-&-fix-wrong-file-end-of-line-encoding.patch

BuildArch:      noarch

BuildRequires:  libappstream-glib
BuildRequires:  vim-filesystem
Requires:       vim-enhanced

%description
Collection of awesome color schemes for Neo/vim, merged for quick use.


%prep
%autosetup -n %{name}-%{commit} -p1


%install
mkdir -p                    %{buildroot}%{vimfiles_root}
cp -pr {autoload,colors}    %{buildroot}%{vimfiles_root}
install -m 0644 -Dp %{SOURCE1}  %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%doc README.md docs/
%{vimfiles_root}/autoload/*
%{vimfiles_root}/colors/*
%{_metainfodir}/*.xml


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20191209gitb5037cb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-8.20191209gitb5037cb
- Remove executable bit & Fix wrong file end of line encoding

* Fri Jan 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-7.20191209gitb5037cb
- Preserve timestamps during copy

* Mon Dec 09 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-6.20191209gitb5037cb
- Update to latest git snapshot
- Add missed license in spec file

* Sun Sep 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-6.20190921git21f5c63
- Initial package
