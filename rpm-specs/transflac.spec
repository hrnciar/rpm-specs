%global owner		gbcox
%global commit		8cd22171e4e0592b7928ce603f7848842918cd88
%global shortcommit	%(c=%{commit}; echo ${c:0:12})

Name:			transflac
Version:		1.0.1
Release:		2%{?dist}
Summary:		Transcode FLAC to lossy formats

License:		GPLv3+
URL:			https://bitbucket.org/%{owner}/%{name}
Source0:		https://bitbucket.org/%{owner}/%{name}/get/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:		%{name}.rpmlintrc

BuildArch:		noarch
Requires:		figlet
Requires:		flac
Requires:		vorbis-tools
Requires:		opus-tools
Requires:		rsync
Requires:		procps-ng
Requires:		coreutils

%description
transflac is a front end command line utility (actually, a bash script)
that transcodes FLAC audio files into various lossy formats.

%prep
%setup -q -n %{owner}-%{name}-%{shortcommit}

%build

%install
%make_install prefix=%{_prefix} sysconfdir=%{_sysconfdir}


%files
%license LICENSE.md
%doc README.md contributors.txt
%config(noreplace) %{_sysconfdir}/transflac.conf
%{_bindir}/transflac
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/src-tf-set-colors.sh
%{_libexecdir}/%{name}/src-tf-ck-codec.sh
%{_libexecdir}/%{name}/src-tf-ck-input.sh
%{_libexecdir}/%{name}/src-tf-ck-output.sh
%{_libexecdir}/%{name}/src-tf-ck-quality.sh
%{_libexecdir}/%{name}/src-tf-codec.sh
%{_libexecdir}/%{name}/src-tf-figlet.sh
%{_libexecdir}/%{name}/src-tf-help.sh
%{_libexecdir}/%{name}/src-tf-terminal-header.sh
%{_libexecdir}/%{name}/src-tf-table.sh
%{_libexecdir}/%{name}/src-tf-progress-bar.sh
%{_mandir}/man1/transflac.1*

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.0.1-1
- Upstream release rhbz#1767252

* Thu Oct 31 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.0.0-3
- Fedora Review rhbz#1767252

* Thu Oct 31 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.0.0-2
- Fedora Review rhbz#1767252

* Wed Oct 30 2019 Gerald Cox <gbcox@fedoraproject.org> - 1.0.0-1
- initial build
