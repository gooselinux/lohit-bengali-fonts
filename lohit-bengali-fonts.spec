%global fontname lohit-bengali
%global fontconf 66-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        2.4.3
Release:        5%{?dist}
Summary:        Free Bengali font

Group:          User Interface/X
License:        GPLv2
URL:            https://fedorahosted.org/lohit/
Source0:        http://pravins.fedorapeople.org/lohit/bengali/%{fontname}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem
Obsoletes: lohit-fonts-common < %{version}-%{release}
Patch1: bug-586854.patch

%description
This package provides a free Bengali truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 
%patch1 -p1 -b .1-fontconf_fix


%build
./generate.pe *.sfd

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%clean
rm -fr %{buildroot}


%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT COPYING AUTHORS README ChangeLog.old


%changelog
* Tue May 04 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.3-5
- Resolves: bug 586854

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.4.3-3.1
- Rebuilt for RHEL 6

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-3
- updated specs

* Wed Sep 09 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball


