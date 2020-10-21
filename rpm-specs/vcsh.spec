%global commit b8bd702362a260c22df3980767460190f8a0b1c1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           vcsh
Version:        1.20151229
Release:        10%{?dist}
Summary:        Version Control System for $HOME

License:        GPLv2+
URL:            https://github.com/RichiH/vcsh
Source0:        https://github.com/RichiH/vcsh/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildArch:      noarch
Requires:       git

BuildRequires:  git


%description
vcsh allows you to have several git repositories, all maintaining their working
trees in $HOME without clobbering each other. That, in turn, means you can have
one repository per config set (zsh, vim, ssh, etc), picking and choosing which
configs you want to use on which machine.


%prep
%setup -qn %{name}-%{commit}


%build
make %{?_smp_mflags}


%install
%{make_install} DOCDIR=%{_pkgdocdir} ZSHDIR=%{_datadir}/zsh/site-functions


%files
%doc LICENSE CONTRIBUTORS changelog
%{_bindir}/%{name}
%{_mandir}/man*/%{name}*
%{_docdir}/*
%{_datadir}/zsh/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.20151229-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 22 2016 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20151229-2
- Declare %%_docdir in %%files

* Wed Feb 10 2016 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20151229-1
- Bumped version to 1.20151229

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.20141026-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20141026-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 26 2014 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20141026-1
- Bumped version to 1.20141026

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20140508-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20140508-1
- Bumped version to 1.20140508
- Switched to a commit tarball from github

* Sun Dec 15 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20131229-1
- Bumped version to 1.20131229

* Sun Dec 15 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20131214-1
- Bumped version to 1.20131214

* Tue Oct 22 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20130909-3
- The Makefile patch has been submitted upstream

* Sat Oct 19 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20130909-2
- Switched to _pkgdocdir
- Removed unnecessary `rm -rf %%{buildroot}' in clean and install

* Sat Oct 12 2013 Dridi Boukelmoune <dridi.boukelmoune@gmail.com> - 1.20130909-1
- Initial package
