%global appdata_dir %{_datadir}/appdata

Name: vim-commentary
Version: 1.3
Release: 8%{?dist}
Summary: Comment and uncomments stuff in Vim using motion as a target
License: Vim
URL: http://www.vim.org/scripts/script.php?script_id=3695
Source0: https://github.com/tpope/vim-commentary/archive/v%{version}/%{name}-%{version}.tar.gz
# Plug-in AppData for Gnome Software.
# https://github.com/tpope/vim-commentary/pull/52
Source1: vim-commentary.metainfo.xml
Requires: vim-common
Requires(post): %{_bindir}/vim
Requires(postun): %{_bindir}/vim
# Needed for AppData check.
BuildRequires: libappstream-glib
# Defines %%vimfiles_root_root
BuildRequires: vim-filesystem
BuildArch: noarch

%description
Comment stuff out. Use gcc to comment out a line (takes a count), gc to
comment out the target of a motion (for example, gcap to comment out a
paragraph), and gc in visual mode to comment out the selection. That's it.

Oh, and it uncomments, too. The above maps actually toggle, and gcgc
uncomments a set of adjacent commented lines.

%prep
%setup -q

%build


%install
mkdir -p %{buildroot}%{vimfiles_root}
cp -pr doc plugin %{buildroot}%{vimfiles_root}

# Install AppData.
mkdir -p %{buildroot}%{appdata_dir}
install -m 644 %{SOURCE1} %{buildroot}%{appdata_dir}

%check
# Check the AppData add-on to comply with guidelines.
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.metainfo.xml

%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%postun
> %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null

%files
%doc CONTRIBUTING.markdown README.markdown
%{vimfiles_root}/doc/*
%{vimfiles_root}/plugin/*
%{appdata_dir}/vim-commentary.metainfo.xml


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 07 2016 Vít Ondruch <vondruch@redhat.com> - 1.3-1
- Update to commentary.vim 1.3.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 07 2015 Vít Ondruch <vondruch@redhat.com> - 1.2-1
- Initial package.
