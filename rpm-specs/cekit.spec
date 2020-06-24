%global modname cekit
%global _description \
CEKit helps to build container images from image definition files

Name:           %{modname}
Version:        3.6.0
Release:        3%{?dist}
Summary:        Container image creation tool
License:        MIT
URL:            https://cekit.io
Source0:        https://github.com/cekit/cekit/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       git

%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-pykwalify
BuildRequires:  python2-colorlog
BuildRequires:  python2-pyyaml
BuildRequires:  python-jinja2

Requires:       python-jinja2
Requires:       python-setuptools
Requires:       python2-pykwalify
Requires:       python2-colorlog
Requires:       python2-pyyaml
Requires:       python2-click
Requires:       python2-packaging
%else
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pykwalify
BuildRequires:  python3-colorlog
BuildRequires:  python3-pyyaml
BuildRequires:  python3-jinja2

Requires:       python3-jinja2
Requires:       python3-setuptools
Requires:       python3-pykwalify
Requires:       python3-colorlog
Requires:       python3-pyyaml
Requires:       python3-click
Requires:       python3-packaging

Suggests:       python3-docker
Suggests:       python3-docker-squash
Suggests:       docker
%endif

%description %_description

%package -n %{modname}-bash-completion
Summary:        %{summary}
Requires:       bash-completion
%description -n %{modname}-bash-completion %_description

Bash completion.

%package -n %{modname}-zsh-completion
Summary:        %{summary}
Requires:       zsh
%description -n %{modname}-zsh-completion %_description

ZSH completion.

%prep
%setup -q -n cekit-%{version}

%if 0%{?rhel} && 0%{?rhel} < 8
# Remove version requirement for packaging
sed -i 's/^packaging.*$/packaging/' requirements.txt
%endif

%build
%if 0%{?rhel} && 0%{?rhel} < 8
%py2_build
%else
%py3_build
%endif

%install
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
cp support/completion/bash/cekit %{buildroot}/%{_sysconfdir}/bash_completion.d/cekit

mkdir -p %{buildroot}/%{_datadir}/zsh/site-functions
cp support/completion/zsh/_cekit %{buildroot}/%{_datadir}/zsh/site-functions/_cekit

%if 0%{?rhel} && 0%{?rhel} < 8
%py2_install
%else
%py3_install
%endif

%files -n %{modname}-bash-completion
%doc README.rst
%license LICENSE
%{_sysconfdir}/bash_completion.d/cekit

%files -n %{modname}-zsh-completion
%doc README.rst
%license LICENSE
%{_datadir}/zsh/site-functions/_cekit

%files -n %{modname}
%doc README.rst
%license LICENSE

%if 0%{?rhel} && 0%{?rhel} < 8
%{python2_sitelib}/cekit/
%{python2_sitelib}/cekit-*.egg-info/
%else
%{python3_sitelib}/cekit/
%{python3_sitelib}/cekit-*.egg-info/
%endif

%{_bindir}/cekit
%{_bindir}/cekit-cache

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Marek Goldmann <mgoldman@redhat.com> - 3.6.0-1
- Release 3.6.0

* Thu Sep 19 2019 Marek Goldmann <mgoldman@redhat.com> - 3.5.0-1
- Release 3.5.0

* Mon Sep 02 2019 Marek Goldmann <mgoldman@redhat.com> - 3.4.0-2
- Specify proper R/BR for PyYAML

* Thu Aug 22 2019 Marek Goldmann <mgoldman@redhat.com> - 3.4.0-1
- Release 3.4.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3.1-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Marek Goldmann <mgoldman@redhat.com> - 3.3.1-1
- Release 3.3.1

* Wed Jun 26 2019 Marek Goldmann <mgoldman@redhat.com> - 3.2.0-1
- Release 3.2.0

* Mon Jun 03 2019 Marek Goldmann <mgoldman@redhat.com> - 3.1.0-1
- Release 3.1.0

* Tue Apr 30 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.1-1
- Release 3.0.1

* Wed Apr 17 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-1
- Release 3.0.0

* Mon Apr 08 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.7.20190408git45cab46
- Updated revision to 45cab46

* Fri Mar 08 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.6.20190308git6318d73
- Rebuild

* Fri Mar 08 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.5.20190308git6318d73
- Rebuild

* Fri Mar 08 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.4.20190308git6318d73
- Updated revision to 6318d73

* Fri Mar 08 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.3.20190308git4f12391
- Updated revision to 4f12391

* Mon Feb 18 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.2.20190214git91cb6c1
- Update to commit dcb561650f177a800208c89e62d029d5ed9cc912
- Added support for RHEL 8 in coditionals
- Fixed Release
- Updated Source

* Thu Feb 14 2019 Marek Goldmann <mgoldman@redhat.com> - 3.0.0-0.1.20190214gitec3a0b
- Initial packaging
