%if %{defined fedora} || (%{defined rhel} && 0%{?rhel} >= 8)
%bcond_without docfiletriggers
%endif

Name: vim-fugitive
Version: 3.0
Release: 3%{?dist}
Summary: A Git wrapper so awesome, it should be illegal
License: Vim
URL: http://www.vim.org/scripts/script.php?script_id=2975
Source0: https://github.com/tpope/vim-fugitive/archive/v%{version}/%{name}-%{version}.tar.gz
# Plug-in AppData for Gnome Software.
# https://github.com/tpope/vim-fugitive/pull/638
Source1: vim-fugitive.metainfo.xml
Requires: vim-common
%if %{without filetriggers}
Requires(post): %{_bindir}/vim
Requires(postun): %{_bindir}/vim
%endif
BuildRequires: vim-filesystem
# Needed for AppData check.
BuildRequires: libappstream-glib
BuildArch: noarch


%description
fugitive.vim may very well be the best Git wrapper of all time. Check out these
features:

View any blob, tree, commit, or tag in the repository with :Gedit (and :Gsplit,
:Gvsplit, :Gtabedit, ...). Edit a file in the index and write to it to stage
the changes. Use :Gdiff to bring up the staged version of the file side by side
with the working tree version and use Vim's diff handling capabilities to stage
a subset of the file's changes.

Bring up the output of git-status with :Gstatus. Press `-` to add/reset a
file's changes, or `p` to add/reset --patch. And guess what :Gcommit does!

:Gblame brings up an interactive vertical split with git-blame output. Press
enter on a line to reblame the file as it stood in that commit, or`o` to open
that commit in a split.

:Gmove does a git-mv on a file and simultaneously renames the buffer. :Gremove
does a git-rm on a file and simultaneously deletes the buffer.

Use :Ggrep to search the work tree (or any arbitrary commit) with git-grep,
skipping over that which is not tracked in the repository. :Glog loads all
previous revisions of a file into the quickfix list so you can iterate over
them and watch the file evolve!

:Gread is a variant of `git checkout -- filename` that operates on the buffer
rather than the filename.  This means you can use `u` to undo it and you never
get any warnings about the file changing outside Vim. :Gwrite writes to both
the work tree and index versions of a file, making it like git-add when called
from a work tree file and like git-checkout when called from the index or a
blob in history.

Add an indicator with the current branch in (surprise!) your statusline.

Oh, and of course there's :Git for running any arbitrary command.


%prep
%setup -q


%install
install -D -p -m 0644 doc/fugitive.txt %{buildroot}%{vimfiles_root}/doc/fugitive.txt
install -D -p -m 0644 plugin/fugitive.vim %{buildroot}%{vimfiles_root}/plugin/fugitive.vim
install -D -p -m 0644 autoload/fugitive.vim %{buildroot}%{vimfiles_root}/autoload/fugitive.vim
install -D -p -m 0644 ftdetect/fugitive.vim %{buildroot}%{vimfiles_root}/ftdetect/fugitive.vim

# Install AppData.
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_metainfodir}/vim-fugitive.metainfo.xml


%check
# Check the AppData add-on to comply with guidelines.
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%if %{without docfiletriggers}
%post
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null


%postun
> %{vimfiles_root}/doc/tags
vim -c ":helptags %{vimfiles_root}/doc" -c :q &> /dev/null
%endif


%files
%doc %{vimfiles_root}/doc/fugitive.txt
%{vimfiles_root}/plugin/fugitive.vim
%{vimfiles_root}/autoload/fugitive.vim
%{vimfiles_root}/ftdetect/fugitive.vim
%{_metainfodir}/vim-fugitive.metainfo.xml


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Carl George <carl@george.computer> - 3.0-1
- Latest upstream

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 12 2019 Carl George <carl@george.computer> - 2.5-1
- Latest upstream

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Carl George <carl@george.computer> - 2.4-3
- Include autoload and ftdetect files from upstream for proper functionality

* Wed Jul 18 2018 Carl George <carl@george.computer> - 2.4-2
- Re-add documentation scriptlets for EPEL

* Wed Jul 18 2018 Carl George <carl@george.computer> - 2.4-1
- Latest upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Vít Ondruch <vondruch@redhat.com> - 2.3-2
- Documentation updates are now handled by Vim transfiletriggers.

* Fri Jun 15 2018 Carl George <carl@george.computer> - 2.3-1
- Latest upstream
- Mark documentation file as %%doc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 24 2016 Brad Hubbard <bhubbard@redhat.com> - 2.2-5
- Fix "E117: Unknown function: netrw#NetrwBrowseX" [1349684]

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Vít Ondruch <vondruch@redhat.com> - 2.2-2
- Remove something like RPM macro from description.

* Tue May 12 2015 Vít Ondruch <vondruch@redhat.com> - 2.2-1
- Initial package.
