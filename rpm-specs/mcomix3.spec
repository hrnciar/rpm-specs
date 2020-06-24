%global		gitcommit		a098f817272443a22ddd80d40b9eb00a0ed429c9
%global		gitdate		20191205
%global		shortcommit	%(c=%{gitcommit}; echo ${c:0:7})

%global		tarballdate	20191230
%global		tarballtime	1643

Name:			mcomix3
# For now, choose version 0
Version:		0
Release:		0.7.D%{gitdate}git%{shortcommit}%{?dist}
Summary:		User-friendly, customizable image viewer for comic books
# GPL version info is from mcomix/mcomixstarter.py
License:		GPLv2+
URL:			https://github.com/multiSnow/mcomix3
# Use git repository directly - with it when modifying source
# we can do it *in git repository* and then we can directly submit
# patch to the upstream by pull request
Source0:		%{name}-%{tarballdate}T%{tarballtime}.tar.bz2
# Source0 is created by Source1
Source1:		create-mcomix3-git-bare-tarball.sh
# Some additional files
Source2:		mcomix3starter.sh
# Borrow some desktop related files
Source10:		mcomix3.desktop
# Patches
Patch1:		0001-Handle-encoding-exception-when-loading-bookmark-pick.patch
Patch2:		0002-Change-domain-name-for-gettext.patch
Patch3:		0003-Search-gettext-files-in-system-wide-directory.patch
Patch4:		0004-Lower-pickle-protocol-version-for-mcomix-compatibili.patch

BuildRequires:	python3-devel
#BuildRequires:	%%{_bindir}/appstream-util
BuildRequires:	%{_bindir}/desktop-file-install
BuildRequires:	gettext
BuildRequires:	git
Requires:		gtk3
Requires:		python3-gobject
Requires:		python3-pillow
BuildArch:		noarch
%if 0%{?fedora} >= 32
Obsoletes:		mcomix < 1.2.2
Obsoletes:		comix < 4.0.5
Provides:		mcomix = 1.2.2
%endif


%description
MComix3 is a user-friendly, customizable image viewer.
It has been forked from the original MComix project and ported to python3.

%prep
%setup -q -c -T -a 0

# Setup source git repository
git clone ./%{name}.git
cd %{name}

git config user.name "%{name} Fedora maintainer"
git config user.email "%{name}-owner@fedoraproject.org"
git checkout -b %{version}-%{release}-fedora %{gitcommit}

# Apply patches
cat %{PATCH1} | git am
cat %{PATCH2} | git am
cat %{PATCH3} | git am
# For now apply this
cat %{PATCH4} | git am

%build
pushd %{name}
rm -rf localroot
mkdir localroot

python3 installer.py --srcdir=mcomix --target=$(pwd)/localroot/
popd

%install
pushd %{name}
cp -p [A-Z]* ..
popd

# Install manually...
SITETOPDIR=%{python3_sitelib}/%{name}
DSTTOPDIR=%{buildroot}${SITETOPDIR}
mkdir -p ${DSTTOPDIR}
mkdir -p ${DSTTOPDIR}/mcomix3
mkdir -p %{buildroot}%{_datadir}/locale
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/

pushd %{name}
rm -rf localroot.2
cp -a localroot localroot.2

pushd localroot.2/mcomix

# Wrapper script
install -cpm 0755 %{SOURCE2} ${DSTTOPDIR}
# locale files
find mcomix/messages/* -type f | while read f
do
	dir=$(dirname $f)
	mv $f $dir/%{name}.mo
done
mv mcomix/messages/* %{buildroot}%{_datadir}/locale/
# duplicate icon
for dir in mcomix/images/*x*/
do
	basedir=$(basename $dir)
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$basedir/apps
	cp -p $dir/*png %{buildroot}%{_datadir}/icons/hicolor/$basedir/apps/%{name}.png
done
# data files
mv mcomix/ ${DSTTOPDIR}/mcomix3/
# Not needed
rm -f comicthumb.py
mv mcomixstarter.py ${DSTTOPDIR}/

# Ensure that all files are installed
popd
rmdir localroot.2/mcomix
rmdir localroot.2

popd
# Wrapper symlink
mkdir %{buildroot}/%{_bindir}
ln -sf ${SITETOPDIR}/mcomix3starter.sh %{buildroot}%{_bindir}/mcomix3
# Desktop file
mkdir %{buildroot}%{_datadir}/applications
desktop-file-install \
	--remove-category Application \
	--dir %{buildroot}%{_datadir}/applications/ \
	%{SOURCE10}

%find_lang %{name}

%files -f %{name}.lang
%license	COPYING
%doc		ChangeLog
%doc		README*
%doc		TODO

%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
# Do not own %%{_datadir}/icons/hicolor explicitly
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
# TODO: appdata file, not availale yet (should item)

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-0.7.D20191205gita098f81
- Rebuilt for Python 3.9

* Fri May  8 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> 0-0.6.D20191205gita098f81
- Pass argument to start script (Patch by Sean Morgan <sean@shellytrail.net>)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.D20191205gita098f81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 30 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> 0-0.4.D20191205gita098f81
- Update to latest git (20191205)

* Fri Nov  8 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> 0-0.2.D20190616git0405a23
- Reflect package review suggestions (bug 1768447)

* Mon Nov 04 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> 0-0.1.D20190616git0405a23
- Initial packaging
