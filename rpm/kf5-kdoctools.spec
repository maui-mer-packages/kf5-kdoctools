# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kf5-kdoctools

# >> macros
# << macros

Summary:    KDE Frameworks 5 Tier 2 addon for documentation
Version:    4.99.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kf5-kdoctools.yaml
Source101:  kf5-kdoctools-rpmlintrc
Patch0:     kdoctools-improve-error-reporting-in-meinproc.patch
Requires:   kf5-filesystem
Requires:   docbook-dtds
Requires:   docbook-style-xsl
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  kf5-karchive-devel

%description
Provides tools to generate documentation in various format from DocBook files.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kf5-karchive-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications |
that use %{name}.


%package doc
Summary:    User documentation and help for %{name}
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation and user help for %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# kdoctools-improve-error-reporting-in-meinproc.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING.LIB README.md
%{_kf5_bindir}/checkXML5
%{_kf5_bindir}/meinproc5
%{_kf5_datadir}/man/*
%{_kf5_datadir}/kf5/kdoctools/customization
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/XsltKde/*
%{_kf5_libdir}/libKF5XsltKde.a
%{_kf5_libdir}/cmake/KF5DocTools
# >> files devel
# << files devel

%files doc
%defattr(-,root,root,-)
%{_kf5_docdir}/HTML/*/kdoctools5-common
# >> files doc
# << files doc
