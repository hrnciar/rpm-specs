%global srcname mnemonic
%global sum Implementation of Bitcoin BIP-0039

Name:           python-%{srcname}
Version:        0.18
Release:        8%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/trezor/python-mnemonic
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%description
This BIP describes the implementation of a mnemonic code or mnemonic sentence -
a group of easy to remember words - for the generation of deterministic wallets.

It consists of two parts: generating the mnenomic, and converting it into a
binary seed. This seed can be later used to generate deterministic wallets using
BIP-0032 or similar methods.

See https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki for full
specification.


%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       python3-pbkdf2
BuildRequires:  python3-pbkdf2
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This BIP describes the implementation of a mnemonic code or mnemonic sentence -
a group of easy to remember words - for the generation of deterministic wallets.

It consists of two parts: generating the mnenomic, and converting it into a
binary seed. This seed can be later used to generate deterministic wallets using
BIP-0032 or similar methods.

See https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki for full
specification.


%prep
%autosetup -n %{srcname}-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%doc PKG-INFO
%doc README.rst
%license LICENSE
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Jonny Heggheim <hegjon@gmail.com> - 0.18-2
- Removed Python2 subpackage

* Wed Jul 18 2018 Jonny Heggheim <hegjon@gmail.com> - 0.18-1
- Updated to version 0.18

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.17-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 09 2017 Jonny Heggheim <jonnyheggheim@sigaint.org> - 0.17-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.15-2
- Rebuild for Python 3.6

* Wed Nov 16 2016 Jonny Heggheim <jonnyheggheim@sigaint.org> - 0.15-1
- Initial package
