%bcond_without check

# https://github.com/junegunn/fzf
%global goipath         github.com/junegunn/fzf
Version:                0.21.1
%global tag             %{version}

%gometa

Name:           fzf
Release:        1%{?dist}
Summary:        A command-line fuzzy finder written in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        README.Fedora

BuildRequires: golang(github.com/gdamore/tcell) >= 1.3
BuildRequires: golang(github.com/gdamore/tcell/encoding)
BuildRequires: golang(github.com/mattn/go-isatty) >= 0.0.12
BuildRequires: golang(github.com/mattn/go-runewidth) >= 0.0.8
BuildRequires: golang(github.com/mattn/go-shellwords) >= 1.0.9
BuildRequires: golang(github.com/saracen/walker)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)

%description
fzf is a general-purpose command-line fuzzy finder.

It's an interactive Unix filter for command-line that can be used with any
list; files, command history, processes, hostnames, bookmarks, git commits,
etc.


%prep
%goprep
cp %{SOURCE1} .


%build
%gobuild -o %{gobuilddir}/bin/fzf %{goipath}

# Cleanup interpreters
sed -i -e '/^#!\//, 1d' shell/completion.*
sed -i -e '1d;2i#!/bin/bash' bin/fzf-tmux


%install
install -vdm 0755 %{buildroot}%{_bindir}
install -vDpm 0755 %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm0755 bin/fzf-tmux %{buildroot}%{_bindir}/
install -d -p %{buildroot}%{_mandir}/man1
install -Dpm0644 man/man1/*.1 %{buildroot}%{_mandir}/man1/

install -d %{buildroot}%{_datadir}/fzf

# Install vim plugin
install -d %{buildroot}%{_datadir}/vim/vimfiles/plugin
install -Dpm0644 plugin/fzf.vim %{buildroot}%{_datadir}/vim/vimfiles/plugin/
install -d %{buildroot}%{_datadir}/nvim/site/plugin
install -Dpm0644 plugin/fzf.vim %{buildroot}%{_datadir}/nvim/site/plugin/

# Install shell completion
install -d %{buildroot}%{_sysconfdir}/bash_completion.d/
install -Dpm0644 shell/completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/fzf
install -d %{buildroot}%{_datadir}/zsh/site-functions
install -Dpm0644 shell/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/fzf

# Install shell key bindings (not enabled)
install -d %{buildroot}%{_datadir}/fzf/shell
install -Dpm0644 shell/key-bindings.* %{buildroot}%{_datadir}/fzf/shell/


%if %{with check}
%check
%gocheck
%endif


%files
%license LICENSE
%doc README.md README-VIM.md CHANGELOG.md README.Fedora
%{_bindir}/fzf
%{_bindir}/fzf-tmux
%{_mandir}/man1/fzf.1*
%{_mandir}/man1/fzf-tmux.1*
%dir %{_datadir}/fzf
%{_datadir}/fzf/shell
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/fzf
%dir %{_datadir}/vim/vimfiles/plugin
%{_datadir}/vim/vimfiles/plugin/fzf.vim
%dir %{_datadir}/nvim/site/plugin
%{_datadir}/nvim/site/plugin/fzf.vim
%{_sysconfdir}/bash_completion.d/fzf


%changelog
* Wed May 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.21.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 11 16:47:31 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.20.0-2
- Fix bash completion installation location (#1789958)

* Mon Dec 23 01:41:54 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.20.0-1
- Update to 0.20.0 (#1784565)

* Sat Nov 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.19.0-1
- Update to latest version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18.0-2
- Update to latest Go macros

* Mon Apr 01 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.18.0-1
- Update to latest version
- Move bash completion to /use/share (#1683868)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.5-2
- Switch to forgesetup

* Wed Oct 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.5-1
- New upstream release.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.17.4-1
- New upstream release.
- Update spec based on More Go Programming template.

* Fri Mar 16 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.17.3-1
- New upstream release.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 22 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.17.1-1
- New upstream release.

* Wed Sep 20 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.17.0.2-1
- New upstream release.

* Mon Sep 4 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.17.0-1
- New upstream release.
- Mention neovim in readme as well.

* Mon Sep 4 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.16.11-7
- Install plugin for neovim also.

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.16.11-6
- Turn off source and unit testing packages.

* Wed Aug 23 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.16.11-5
- Enable vim plugin by default.
- Fix directory ownership on plugins.

* Mon Aug 21 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.16.11-4
- Restore dist tag.

* Sun Aug 20 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.16.11-3
- Fix source URL.
- Enable debuginfo subpackage.
- Correct interpreters in shebangs.

* Sun Aug 20 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.16.11-2
- Add fzf binary to package.
- Add Fedora-specific readme about optional things.
- Install shell completions.
- Install (disabled) vim plugin also.
- Install (disabled) shell key bindings.

* Fri Aug 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.16.11-1
- Initial package for Fedora
