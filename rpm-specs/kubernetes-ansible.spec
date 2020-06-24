%global provider	github
%global provider_tld	com
%global project		kubernetes
%global repo		contrib
# https://github.com/kubernetes/contrib
%global provider_prefix	%{provider}.%{provider_tld}/%{project}/%{repo}
%global commit		19584618dffa77ed7c4f5db59c689fce023e24f8
%global shortcommit	%(c=%{commit}; echo ${c:0:7})

Name:		kubernetes-ansible
Version:	0.7.0
Release:	0.11.git%{shortcommit}%{?dist}
Summary:	Playbook and set of roles for seting up a Kubernetes cluster onto machines
License:	ASL 2.0
URL:		https://%{provider_prefix}
Source0:	https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

Patch0:         Enable-libvirt-provider-only.patch
Patch1:         make-some-kubelet-args-configurable.patch

BuildArch:	noarch

Requires:       ansible
Requires:       python3-netaddr

Conflicts:      %{name} < 0.7.0

%description
%{summary}

%package vagrant
Summary: Deploy kubernetes vith Vagrant
Requires: %{name} = %{version}-%{release}
Requires: vagrant-libvirt ruby-devel gcc redhat-rpm-config

%description vagrant
The Vagrant runs playbooks specified in %{name}.

%prep
%setup -q -n %{repo}-%{commit}
%patch0 -p1
%patch1 -p1

%build

%install
install -m 755 -d %{buildroot}%{_datadir}/%{name}
pushd ansible
cp -rp inventory %{buildroot}%{_datadir}/%{name}/
cp -rp roles %{buildroot}%{_datadir}/%{name}/
cp -rp playbooks %{buildroot}%{_datadir}/%{name}/
cp -rp scripts %{buildroot}%{_datadir}/%{name}/
cp -rp vagrant %{buildroot}%{_datadir}/%{name}/
popd

%check

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc ansible/README.md
%{_datadir}/%{name}/inventory
%{_datadir}/%{name}/roles
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/playbooks
%dir %{_datadir}/%{name}

%files vagrant
%license LICENSE
%doc ansible/vagrant/README.md
%{_datadir}/%{name}/vagrant

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.11.git1958461
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-0.10.git1958461
- Require Python 3 version of netaddr, Ansible runs on Python 3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.9.git1958461
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.8.git1958461
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.7.git1958461
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.0-0.6.git1958461
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.5.git1958461
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.4.git1958461
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-0.3.git1958461
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 03 2016 jchaloup <jchaloup@redhat.com> - 0.7.0-0.2.git1958461
- cherry-pick #1812 to make some kubelet args configurable

* Fri Sep 09 2016 jchaloup <jchaloup@redhat.com> - 0.7.0-0.1.git1958461
- Update to v0.7.0 + cherry-pick ansible changes
  Introduce vagrant subpackage

* Wed Aug 17 2016 jchaloup <jchaloup@redhat.com> - 0.6.0-0.2.gitd65ebd5
- python-netaddr is required by ipaddr filter
  resolves: #1367778

* Tue May 31 2016 jchaloup <jchaloup@redhat.com> - 0.6.0-0.1.gitd65ebd5
- Package kubernetes/contrib/ansible
  resolves: #1341310
